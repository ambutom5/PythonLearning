# f = open("Demo.txt","x")
# f.close()

file = open("Demo.txt","w")
file.write("Hello World!")
file.close()

f1 = open("Demo.txt")
print(f1.read())