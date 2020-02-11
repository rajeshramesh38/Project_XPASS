import json

value = {'A': [(3, 0), (2, 0), (1, 0), (0, 1), (0, 2), (1, 3), (2, 3), (3, 3), (2, 0), (2, 1), (2, 2), (2, 3)]}
with open("dataset.json", "r") as maps:
    dataset = json.load(maps)
    print(dataset.items())
