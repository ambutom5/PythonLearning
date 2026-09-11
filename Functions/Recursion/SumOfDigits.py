def sumdigits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sumdigits(n//10)

print(sumdigits(12345))

#     Working
# ----------------
# For example, with 12345:
# 5 + sum_of_digits(1234)
# 5 + (4 + sum_of_digits(123))
# 5 + 4 + (3 + sum_of_digits(12))
# 5 + 4 + 3 + (2 + sum_of_digits(1))
# 5 + 4 + 3 + 2 + 1 = 15