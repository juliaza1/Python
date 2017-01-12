import re
import sys

# Open files for reading
ifile = open (sys.argv[1])  # original
ofile = open (sys.argv[2])  # modified
out = open('out.txt', 'w')  # output

# Reading lines
ilines = ifile.readlines()
olines = ofile.readlines()

lastOlineIdx = 0

# Go through the original file line by line
for iline in ilines:
    # Make a regex pattern of the line
    pattern = re.compile(iline)
    match = False

    # Search through the modified file for the current input line
    # If not found, the line has been removed. If found later, all lines
    # in between has been added

    added = []
    tmpIdx = lastOlineIdx

    for oline in olines[lastOlineIdx:]:
        matchLine = pattern.match(oline)

        if matchLine:
            match = True
            lastOlineIdx = tmpIdx + 1
            break

        added.append(oline)
        tmpIdx += 1

    if not match:
        out.write("- " + iline)
    else:
        for addedLine in added: 
            out.write("+ " + addedLine)

        out.write("0 " + iline)

out.write("\n")

# The rest of olines is now added, print them as such
for remain in olines[lastOlineIdx:]:
    out.write("+ " + remain)

