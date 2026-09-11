n = int(input())

def fibonacci(n):
    mylist = []
    a = 0
    b = 1
    for i in range(n):
        # print(a)
        mylist.append(a)
        c = a + b
        a = b
        b = c
    return mylist
    # return a list of fibonacci numbers

print(list(map(lambda x:x**3, fibonacci(n))))

