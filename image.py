import requests
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

def get_pexels_image_using_query(query, API_KEY="", return_author=True):
    photos = request_pexels_images(query, {"Authorization": API_KEY})
    if len(photos) == 0: #failsafe
        print("No Images found using "+query+", searching for \"nature\" instead.")
        photos = request_pexels_images("nature", {"Authorization": API_KEY})

    image = random.choice(photos)

    downloaded_image = download_image(image["src"]["original"])

    if return_author:
        return downloaded_image, image["photographer"]
    else:
        return downloaded_image

def request_pexels_images(query, header, n_images=15):
    url = "https://api.pexels.com/v1/search?query="+query+"&per_page="+str(n_images)+"&orientation=square&locale=\"en-US\""
    req = requests.get(url, header).json()
    return req["photos"]

def download_image(url):
    image = Image.open(requests.get(url, stream=True).raw)
    return image

def place_text_on_image(image, text, draw_outline=False):
    font = ImageFont.truetype("fonts/Aldi-Bold.otf", 70)

    wrapped_text = wrap_text(text, linewidth=18)

    draw = ImageDraw.Draw(image)
    if draw_outline:
        draw.multiline_text((image.width/2-1, image.height/2), wrapped_text, fill="black", anchor="mm", font=font, align="center")
        draw.multiline_text((image.width/2+1, image.height/2), wrapped_text, fill="black", anchor="mm", font=font, align="center")
        draw.multiline_text((image.width/2, image.height/2-1), wrapped_text, fill="black", anchor="mm", font=font, align="center")
        draw.multiline_text((image.width/2, image.height/2+1), wrapped_text, fill="black", anchor="mm", font=font, align="center")
    draw.multiline_text((image.width/2, image.height/2), wrapped_text, fill="white", anchor="mm", font=font, align="center")
    return image

def wrap_text(text, linewidth=18):
    wrapped = textwrap.wrap(text, width=linewidth)
    wrapped_n = ""
    for w in wrapped:
        wrapped_n += w + "\n"
    wrapped_n = wrapped_n[:-1]
    return wrapped_n
