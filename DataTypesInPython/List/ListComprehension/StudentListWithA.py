students = ["Althaf","Minu","Manu","Anu","Keerthi"]
mylist = []
# newlist = []

for name in students:
    if 'a' in name or 'A' in name:
        mylist.append(name)
print(mylist)


newlist = [name for name in students if 'a' in name or 'A' in name]
print(newlist)



