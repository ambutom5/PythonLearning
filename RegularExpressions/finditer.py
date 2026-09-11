# Purpose: Finds all matches and returns an iterator of match objects.
# Use re.finditer() when you want all matches with positions.

import re

for m in re.finditer("t","Python is easy to learn and study!"):
    print((m.start(),m.end()))


sentence = "Python111 ttt"
x = re.finditer(r"([a-zA-Z0-9])\1{2}",sentence)
for m in x:
    print((m.group(1),m.group(0),m.start(),m.end()))