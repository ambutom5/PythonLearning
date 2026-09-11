def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(12,15))
# 3

# gcd(48, 18)
# gcd(48, 18) → calls gcd(18, 48 % 18) → gcd(18, 12)
# gcd(18, 12) → calls gcd(12, 18 % 12) → gcd(12, 6)
# gcd(12, 6) → calls gcd(6, 12 % 6) → gcd(6, 0)
# gcd(6, 0) → base case → returns 6
# So, GCD(48, 18) = 6 ✅