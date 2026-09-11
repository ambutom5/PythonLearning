x = map(lambda n:n//2,filter(lambda n:n%2,range(8)))
print(sum(x))

# Step 1: range(8)
# This generates numbers from 0 to 7.
# Step 2: filter(lambda n: n % 2, range(8))
# lambda n: n % 2 returns True for odd numbers (since odd % 2 = 1).
# filter() keeps only those numbers where the lambda returns True.
# [1, 3, 5, 7]

# Step 3: map(lambda n: n // 2, [1, 3, 5, 7])
# Now each odd number is divided by 2 using integer division (//):
# 1 // 2 = 0
# 3 // 2 = 1
# 5 // 2 = 2
# 7 // 2 = 3

# So the mapped result is:
# sum([0, 1, 2, 3])
# 0 + 1 + 2 + 3 = 6
# 6