# 6. Write a program to rotate a list to the left by k positions.

mylist = [4,5,1,2,3]
k = 11

k = k % len(mylist)
print("Rotate By",k,"Positions")

newlist = mylist[k:] + mylist[:k]
print(newlist)

