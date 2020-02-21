def is_printable():
    pass


def postprocess(generated_password):
    return_string = ""
    for character in generated_password:
        if is_printable(character):
            return_string += character
    return return_string

