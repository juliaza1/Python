import sys
import re
from helpers import highlight, applyStartCodes

# argv is commandline arguments, argv[0] is program name
if (len(sys.argv) == 4):
    # Reads line by line
    with open(sys.argv[-3], "r") as syn:
        syntax = syn.read().splitlines()
        syn.close()

    with open(sys.argv[-2], "r") as them:
        theme = them.read().splitlines()
        them.close()

    # reads whole file
    with open(sys.argv[-1], "r") as sour:
        source = sour.read()
        sour.close()
else:
    print("Wrong number of inputs. Exiting.")

regEx = []
codeword = []
colour = []

# Regex-patterns for first part and last word
regFirst = r'[^\"].*(?=\")'  # regex inbetween "..."
regLast = r"\w+$"  # codeword
regColour = r"\d+;\d+;?(\d+)?"  # colourcode

# reading matches into two lists
for elem in syntax:
    codeword.append(re.search(regLast, elem).group())
    regEx.append(re.search(regFirst, elem).group())

# creating dict for regExes
dict_RegEx_Code = {k: v for k, v in zip(codeword, regEx)}

i = 0

for elem in theme:
    if (elem.startswith(codeword[i])):
        colour.append(codeword[i])
        colour.append(re.search(regColour, elem).group())
        i += 1

# creating a dictionary for the colours
dict_Code_Colour = dict(colour[i:i + 2] for i in range(0, len(colour), 2))

blocks = []
# Go through the regexp dictionary, and perform highlighting for all of them
for toMatch in dict_RegEx_Code:
    # Get the regex string and the correct color code for the codeword
    matching = dict_RegEx_Code[toMatch]
    code = dict_Code_Colour[toMatch]

    blocks = highlight(source, matching, code)

source = applyStartCodes(source, blocks)

# Dump the resulting highlighted string to the output
print(source)
