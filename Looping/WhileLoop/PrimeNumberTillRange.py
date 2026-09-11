upper = int(input("Enter the upper limit: "))

for num in range(2,upper+1):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i = i + 1
    else:
        print(num)


# OR
#
# for num in range(2,upper+1):
#     flag = 0
#     i = 2
#     while i < num:
#         if num % i == 0:
#             flag = 1
#             break
#         i = i + 1
#     if flag == 0:
#         print(num)





