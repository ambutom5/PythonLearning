s = "ABCDCDC"
sub = "CDC"

count = start = 0

while True:
    start = s.find(sub, start)
    if start == -1:
        break
    count += 1
    start += 1   # move forward by 1 to allow overlap

print(count)     # Output: 2



