# First way
# import re
#
# with open("text.txt") as file:
#     text = file.readlines()
#
# pattern = r"[-,.!?]"
# for index in range(len(text)):
#
#     if index % 2 == 0:
#         current_line = text[index].rstrip()
#         replaced_line = re.sub(pattern, "@", current_line).split()
#         replaced_line.reverse()
#         print(" ".join(replaced_line))

# Second way to get the reversed result
# import re
#
# with open("text.txt") as file:
#     text = file.readlines()
#
# pattern = r"[-,.!?]"
# for index in range(len(text)):
#     if index % 2 == 0:
#         replaced_line = text[index].rstrip()
#         replaced_line = re.sub(pattern, "@", replaced_line)
#         print(" ".join(replaced_line.split()[::-1]))

## Third way
import re

with open("text.txt") as file:
    text = file.readlines()

pattern = r"[-,.!?]"
for index in range(len(text)):

    if index % 2 == 0:
        current_line = text[index].rstrip()
        replaced_line = re.sub(pattern, "@", current_line)
        print(" ".join(reversed(replaced_line.split())))
