from str2hex import hexint

split_len = 2  # Character Splitting length


def encoder(pwds):
    en_str = ""
    for pwd in pwds:
        for index in range(0, len(pwd), split_len):
            en_str += chr(hexint(pwd[index:index + 2]))
    return en_str
