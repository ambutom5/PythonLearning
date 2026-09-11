def factorial(n):
    if n == 0:                                              # Base
        return 1
    return n * factorial(n-1)                               # Recursion Call

print(factorial(5))