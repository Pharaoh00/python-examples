# from sys module import a member called 'argv'
from sys import argv
#unpack
script, filename = argv
# A more clean and modern Python 3 to write to file.
with open(filename, "w") as f:
    print("Writing to file: ".format(filename)) # As python 3+
    f.write("Hello World")
