import random

hexDigits = "0123456789ABCEDF"


def randomizer(string):
    rand_text = ""
    while len(rand_text) < len(string):
        x = random.choice(string)
        if x not in rand_text:
            rand_text += x
    return rand_text


def random_matrix(value):
    matrix = list()
    temp = []
    for x in randomizer(value):
        temp.append(x)
        if len(temp) == 4:
            matrix.append(temp)
            temp = []
    return matrix
