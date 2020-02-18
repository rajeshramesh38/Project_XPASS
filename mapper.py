import json

from splitnencode import encoder

mapper_matrix = [['C', 'D', 'E', 'F'],
                 ['8', '9', 'A', 'B'],
                 ['4', '5', '6', '7'],
                 ['0', '1', '2', '3']]


def mapping(password, patterns):
    temp = password.upper()
    encoded = []
    for letter in temp:
        mappings = patterns[letter]
        secret = ""
        for map in mappings:
            secret += mapper_matrix[map[0]][map[1]]
        encoded.append(secret)
        # encoded.append((letter, secret))
    return encoded

passwd=input("user password")
d = open("dataset.json", "r")
data = json.load(d)
patterns = data
mapped = mapping(passwd, patterns)
print(encoder(mapped))
del d,data,patterns,mapped

