import json

d = open("dataset.json", "r")
data = json.load(d)
patterns = data

def mapping(password, mapper_matrix, patterns=patterns):
    temp = password.upper()
    encoded = []
    for letter in temp:
        mappings = patterns[letter]
        secret = ""
        for map in mappings:
            secret += mapper_matrix[map[0]][map[1]]
        encoded.append(secret)
    return encoded

del d, data, patterns
