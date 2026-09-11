s = "This is a python program"
r = ""

for i in range(len(s)-1,-1,-1):
    r = r + s[i]

print(r)