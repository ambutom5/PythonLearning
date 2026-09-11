n = 11
m = 33

for i in range(1,n,2):
    print((".|." * i).center(m,"-"))

print("WELCOME".center(m,"-"))

for i in range(n-2,0,-2):
    print((".|." * i).center(m,"-"))


# 🔄 Example with n = 7
# Top half loop: range(1, 7, 2) → [1, 3, 5]
# Middle row: printed separately
# Bottom half loop: range(5, 0, -2) → [5, 3, 1]
# This mirrors the top half perfectly.


print()

n= 11
m=33
for i in range(1,n,2):
    print(("***"*i).center(m,"-"))
print("WELCOME HOME HAPPY HOME".center(m,"-"))
for i in range(n-2,0,-2):
    print(("***"*i).center(m,"-"))