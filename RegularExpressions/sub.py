# Purpose: Replace matches with something else.
# Use re.sub() when you want to clean or transform text.

import re
sentence = "Introduction to Python"
x = re.sub(" ","_",sentence)
print(x)

result = re.sub(r"[,.]"," ","100,000.000")
print(result)

result = re.sub(r"[,.]","\n","100,000.000")
print(result)
