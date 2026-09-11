def fibanocci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibanocci(n-1) + fibanocci(n-2)

n = 5

for i in range(n):
    print(fibanocci(i),end = " ")




# ----------Working---------
    # fibonacci(0) = 0
    # fibonacci(1) = 1
    # fibonacci(2) → 1 + 0 -> 1
    # fibonacci(3) → 1 + 1 -> 2
    # fibonacci(4) → 2 + 1 -> 3
    # fibonacci(5) → 3 + 2 -> 5