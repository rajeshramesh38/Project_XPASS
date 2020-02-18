# This program to convert hexa-decimal string to integer
# AF (hex) => 175 (int)
buffer = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
          '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
          'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111",
          }


def hexint(number):
    number=number.upper()
    bin_form = ""
    for num in number:
        if num in buffer:
            bin_form = bin_form + buffer[num]
    count, i = 0, 0
    # print(f'Binary form {bin_form}')
    for x in range(len(bin_form) - 1, -1, -1):
        if bin_form[x] == "1":
            count = count + 2 ** i
        i += 1
    return count

