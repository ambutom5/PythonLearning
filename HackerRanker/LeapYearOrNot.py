year = 2012

# 2024: Divisible by 4, but not by 100 — Leap Year.
# 1900: Divisible by 4 and by 100, but not by 400 — Not a Leap Year.
# 2000: Divisible by 4, by 100, and by 400 — Leap Year.
# 2026: Not divisible by 4 — Not a Leap Year.

flag = True

if year % 4 != 0:
    flag = False
elif year % 100 == 0 and year % 400 != 0:
    flag = False

print(flag)
