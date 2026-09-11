# 9. Write a program to find the missing number from a list containing numbers
# from 1 to N.

nums = [1, 2, 4, 5]  # Missing number is 3
N = 5  # Numbers should be from 1 to 5

def find_missing_number(nums, N):
    # Expected sum of numbers from 1 to N
    expected_sum = N * (N + 1) // 2

    # Actual sum of the given list
    actual_sum = sum(nums)

    # Missing number is the difference
    return expected_sum - actual_sum

print("Missing number:", find_missing_number(nums, N))


# list1 = [2,3,5,7,8,1]
# n = int(input("Enter a number: "))
#
# for i in range(1,n+1):
#     if i not in list1:
#         print(i)