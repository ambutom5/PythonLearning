f = open("Demo.txt")
data = f.readlines()
print(data)
for i in data:
    print(i.strip())
f.close()

print()
f = open("Demo.txt")
data = f.readline()
print(data)
f.close()


