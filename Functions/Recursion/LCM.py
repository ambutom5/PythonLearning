def lcm(a,b,multiple=None):
    # Initialize multiple with the larger of a or b
    if multiple is None:
        multiple = max(a,b)
    # Base case: if multiple is divisible by both a and b
    if multiple % a == 0 and multiple % b == 0:
        return multiple
    else:
        return lcm(a,b,multiple + max(a,b))

print(lcm(3,4))


# Example Trace for lcm(12, 18)
# Start with max(12, 18) = 18
# 18 % 12 != 0 → not divisible → recurse
# Next multiple = 18 + 18 = 36
# 36 % 12 == 0 and 36 % 18 == 0 → ✅ divisible → return 36
# So, LCM(12, 18) = 36.

