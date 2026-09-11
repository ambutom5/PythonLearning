# Print the first occurrence of the repeating character.
# If there are no repeating characters, print -1.

import re

s = "AA1223456789210111213141516171820212223"

pattern = r"([a-zA-Z0-9])\1"

match = re.search(pattern,s)
print(match)

if match:
    print(match.group((0)))
    print(match.group((1)))
else:
    print(-1)