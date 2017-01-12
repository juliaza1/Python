import re
# All blocks of highlights [start, end, code]
highlightBlocks = []

def applyStartCodes(source, blocks):
    vec = []

    # Sort the blocks vector with the smalles blocks first. This makes sure that
    # matchBlock will match the smalles possible outter group, which is what we want
    # to achieve (i.e string inside function call inside comment etc.)
    blocks.sort(key=lambda b: b[1]-b[0])

    # Go through all blocks, and split them into simpler [idx, string] pairs.
    # This enables us to treat starts and ends equally, so that we can sort them
    # properly to insert into the target string in reverse order
    for highlight in blocks:
        start = highlight[0]
        end = highlight[1]
        code = highlight[2]

        existingCode = matchBlock(start, end, blocks)

        # Always start our own colour code at the beginning of the block
        vec.append([start, "\033[{}m".format(code)])

        endCode = "\033[0m"

        # If we are inside an existing block, we append the start code
        # of the outter block after the termintation of our own colour coding
        if existingCode != -1:
            endCode += "\033[{}m".format(existingCode)

        # schedule the end code to be inserted at the end index
        vec.append([end, endCode])

    # start inserting from the back
    vec.sort(key=lambda p: -p[0])

    # Go through all codes to insert (in reverse order because of the sorting)
    for highlight in vec:
        start = highlight[0]
        code = highlight[1]

        first = source[:start]
        second = source[start:]

        # Inject the colour code here. We can do this, since we are only afftecting 
        # indexes in the string that has already been processed. Not that if we did not do 
        # this in the reverse order, the result would be wrong, since the inserted colour codes
        # would be at shifted positions because of the previous inserts. This would look funny.
        source = first + code + second

    return source


# Returns the containing blocks code if start,end is within an existing block
# otherwise -1
def matchBlock(start, end, blocks):
    for existing in blocks:
        if start > existing[0] and end <= existing[1]:
            return existing[2]

    return -1

def replace(text, code):
    # Get the number of groups in the match
    numGroups = len(text.groups())
    
    for idx in range(numGroups or 1):
        start = text.start(idx)
        end = text.end(idx)

        highlightBlocks.append([start, end, code])

    return str(text)

def colour_print(code=5):
    # Make a lambda function that we can pass into re.sub, that will mark the matched
    # groups with the correct colour coded blocks
    return lambda text: replace(text, code)

def highlight(source, matching, code):
    # Mark all highlighting groups using the colour_print callback
    re.sub(matching, colour_print(code), source, flags=re.M)

    return highlightBlocks

