# Purpose: Splits a string by the regex pattern.
# Use re.split() when you want to break text into chunks.

import re
sentence = "Introduction to python"

x = re.split(" ",sentence)
print(x)

y = re.split("to",sentence)
print(y)

parts = re.split(r"[,.]","100,000,000.000")
print("\n".join(parts))