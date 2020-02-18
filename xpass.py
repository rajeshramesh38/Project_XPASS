import json
import sys

cmd_arguments = sys.argv[1:]
pattern_file = open("patterns.json", "r")
patterns = json.load(pattern_file)


def pattern_printer(lt):
    print("---------")
    for row in lt:
        print(end="|")
        for col in row:
            print(col, end="|")
        print()
    print("---------")


if len(cmd_arguments) > 0:
    if cmd_arguments[0] == "help":
        print("""
        Usage:> xpass.py [options] [arguments]
        Options:
            generate_password [pattern] password -> used to generate new strong password (eg. generate_password 1 old_password)
            show_pattern [pattern]               -> used to show the x-matrix patterns (eg. show_pattern 1 to show pattern 1)
            help                                 -> used to help with the documentation  
        """)
    if cmd_arguments[0] == "show_pattern":
        pattern_printer(patterns[cmd_arguments[1]])
    if cmd_arguments[0] == "generate_password":
        pattern_to_choose = patterns[cmd_arguments[1]]
        password = cmd_arguments[2]
else:
    print("Invalid commandline usage")

# while True:
#     if start == "" or start == None or start == "exit" or start == "EXIT" or start == "Exit":
#         print("Cancelled")
#         break
#     else:
#         print(randomizer.randomizer("ABCDEF0123456789"))
#     start = input()
