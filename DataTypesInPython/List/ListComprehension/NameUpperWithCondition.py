list1 = ["Anu","Ambu Tom"]

mylist = [name.upper() for name in list1 if ' ' not in name]
print(mylist)

newlist = [name.title() for name in list1 if ' ' in name]
print(newlist)