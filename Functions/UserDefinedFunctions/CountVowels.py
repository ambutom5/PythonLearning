def count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count +=1
    return count

print(count_vowels("This is a python program"))


OR


# def count_vowels(string):
#     count = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             count +=1
#     return count
#
# print("Enter a string")
# print(count_vowels("This is a python program"))

