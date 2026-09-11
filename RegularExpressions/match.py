# Purpose: Checks if the pattern matches at the beginning of the string.
# Use re.match() when you want to test the start of a string.

import re
sentence = "Python"
s = "Py"

match = re.match(s,sentence)
print(match)

if match:
    print(f"{match.group()} {match.start()}:{match.end()}")
