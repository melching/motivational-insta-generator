from quote import read_from_file
from keywords import get_keywords_using_embedding_similarity, pad_keywords
from image import get_pexels_image_using_query, place_text_on_image
# from insta import post_image
from time import time
import random

# get quote
quote = read_from_file("quotes.txt")

# get keywords
keywords = get_keywords_using_embedding_similarity([quote["author"], quote["text"]], top_n=5)
keywords = pad_keywords(keywords, padding=["nature", "inspirational"])
random.shuffle(keywords)

# get image
image, photographer = get_pexels_image_using_query(" ".join(keywords))

# draw quote
image = place_text_on_image(image, quote["text"], draw_outline=True)

# save image
path = "./images/"+quote["author"]+str(time())+".png"
image.save(path)

# prepare description
desc = "Quote by: " + quote["author"] + ".\nBackground by: " + photographer + ".\n"
for key in keywords:
    desc += "#" + key + " "

# post on insta
# print(desc)