"""
to run this program, open terminal on this folder location and run command
    "python main.py -u -g hello_world"
where python is the keyword to run the main.py file, and everything after python will be treated as an input from terminal
"""


import sys

print(sys.argv) # returns a list of inputs
print(type(sys.argv)) # returns a type list


if "-g" in sys.argv:
    print("Install dependency globally")