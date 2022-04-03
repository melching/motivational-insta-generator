import json
import random

def read_from_file(path, n=1):
    with open(path, "r") as file:
        data = file.read()
    quotes = json.loads(data)

    if n is 1:
        return random.choice(quotes)
    elif n is 0:
        return quotes
    else:
        return random.sample(quotes, n)