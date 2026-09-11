# Given an integer,N, print the following values for each integer
# from 1 to N:
#
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


n = 17
width = len(bin(n))-2
for i in range(1, n + 1):
    print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=width))



# 0 → Refers to the first argument passed into .format(), which is i.
# {w} → A named placeholder for the width.
# When you call .format(i, w=width), the w gets replaced by the value of width.

# d → Format type for decimal integer.
# o → Format type for octal.
# X → Format type for hexadecimal (uppercase).
# b → Format type for binary.