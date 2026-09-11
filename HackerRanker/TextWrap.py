string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_width = 4
mystring = []

for i in range(0,len(string),max_width):
    mystring.append(string[i:i+max_width])
print("\n".join(mystring))


# First loop: i = 0
# → string[0:4] → characters at positions 0,1,2,3 → "ABCD"

# Next loop: i = 4
# → string[4:8] → characters at positions 4,5,6,7 → "EFGH"

# Next loop: i = 8
# → string[8:12] → characters at positions 8,9,10,11 → "IJKL"



# s = "Python"
# print(s[0:4])   # 'Pyth'
# print(s[2:5])   # 'tho'
# print(s[:3])    # 'Pyt'   (start defaults to 0)
# print(s[3:])    # 'hon'   (end defaults to end of string)
