import json
import sys

import mapper
import post_processor
import randomizer
import splitnencode

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


rd_matrix = randomizer.random_matrix()
if len(cmd_arguments) > 0:
    if cmd_arguments[0] == "help":
        print("""
Usage:> xpass.py [options] [arguments]
Options:
    generate_password [pattern] password -> used to generate new strong password (eg. generate_password 1 old_password)
    show_pattern [pattern]           -> used to show the x-matrix patterns (eg. show_pattern 1 to show pattern 1)
    help                             -> used to help with the documentation  
""")
    if cmd_arguments[0] == "show_pattern":
        if cmd_arguments[1] == "random_pattern":
            pattern_printer(rd_matrix)
        else:
            pattern_printer(patterns[cmd_arguments[1]])
    if cmd_arguments[0] == "generate_password":
        pattern_to_choose = list()
        if cmd_arguments[1] == "random_pattern":
            pattern_to_choose = rd_matrix
        else:
            pattern_to_choose = patterns[cmd_arguments[1]]
        password = cmd_arguments[2]
        print(password)
        encoded_form = mapper.mapping(password, pattern_to_choose)
        print(encoded_form)
        gen = splitnencode.encoder(encoded_form)
        print("Not Processed: ", gen, len(gen))
        post_processed = post_processor.postprocess(gen)
        print("Generated Password: ", post_processed, len(post_processed))
else:
    print("Invalid commandline usage please type 'xpass.py help' ")
