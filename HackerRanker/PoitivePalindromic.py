# You are given a space separated list of integers.
# If all the integers are positive, then you need to check
# if any integer is a palindromic.

n = int(input().strip())
list1 = list(map(int, input().split()))
result = all(i>0 for i in list1) and any(str(item)==str(item)[::-1] for item in list1)
print(result)

# OR

# n = int(input().strip())
# list1 = list(map(int, input().split()))

# if all(i > 0 for i in list1):
#     if any(str(item) == str(item)[::-1] for item in list1):
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")