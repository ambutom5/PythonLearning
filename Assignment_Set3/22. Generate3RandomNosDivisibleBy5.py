# 22. Generate 3 random integers between 100 and 999 which is divisible by 5

import random
numbers = random.sample(range(100,999,5),3)
print(numbers)

mylist = []
while len(mylist)<3:
    num = random.randint(100,999)
    if num % 5 == 0:
        mylist.append(num)
print(mylist)

