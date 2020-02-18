import json
import sys

cmd_arguments = sys.argv[1:]


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
        Usage:> xpass [options] [arguments]
        Options:
            generate_password -> used to generate password
            show_pattern      -> used to show the x-matrix patterns
            help              -> used to help with the documentation  
        """)
    if cmd_arguments[0] == "show_pattern":
        pattern_file = open("patterns.json", "r")
        patterns = json.load(pattern_file)
        pattern_printer(patterns[cmd_arguments[1]])
    if cmd_arguments[0] == "generate_password":
        pass
else:
    print("Invalid commandline usage")

# while True:
#     if start == "" or start == None or start == "exit" or start == "EXIT" or start == "Exit":
#         print("Cancelled")
#         break
#     else:
#         print(randomizer.randomizer("ABCDEF0123456789"))
#     start = input()
