import random


def randomizer(string):
    rand_text = ""
    while len(rand_text) < len(string):
        x = random.choice(string)
        if x not in rand_text:
            rand_text += x
    return rand_text
