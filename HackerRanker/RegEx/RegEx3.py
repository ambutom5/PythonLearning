import re

s = "Pyttthon is a hhhigh levell pgmng langauge"
k = "high"

matches = list(re.finditer(k, s))
if matches:
    for m in matches:
        for i in range(m.start(),m.start()+len(k)):
            print((i,i+1))
else:
    print((-1,-1))


