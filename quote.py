import json
import random

def read_from_file(path, n=1):
    with open(path, "r") as file:
        data = file.read()
    quotes = json.loads(data)

    if n == 1:
        quotes = random.choice(quotes)
    elif n == 0:
        quotes = quotes # redundant, but keeping for explainability
    else:
        quotes = random.sample(quotes, n)

    if isinstance(quotes, list):
        for q in quotes:
            if q["author"] is None:
                q["author"] = "Unknown author"
    else:
        if quotes["author"] is None:
            quotes["author"] = "Unknown author"
    
    return quotes
