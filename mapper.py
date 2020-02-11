password = input("user password?")
mapper_matrix = [['C', 'D', 'E', 'F'], ['8', '9', 'A', 'B'], ['4', '5', '6', '7'], ['0', '1', '2', '3']]
patterns = {'A': [(3, 0), (2, 0), (1, 0), (0, 1), (0, 2), (1, 3), (2, 3), (3, 3), (2, 0), (2, 1), (2, 2), (2, 3)]}


def mapping(password):
    temp = password.upper()
    for letter in temp:
        mappings = patterns[letter]
        secret = ""
        for map in mappings:
            secret += mapper_matrix[map[0]][map[1]]
    return secret


split = range(2)
mapped = mapping(password)
