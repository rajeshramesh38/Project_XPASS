def is_printable(character):
    if ord(character) in [x for x in range(0, 32)] + [x for x in range(127, 160)] + [65532]:
        return False
    else:
        return True


def postprocess(generated_password):
    return_string = ""
    for character in generated_password:
        if is_printable(character):
            return_string += character
    return return_string
