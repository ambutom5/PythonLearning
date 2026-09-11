# Your task is to sort the string  in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# ginortS1324

s = "Sorting1234"
str1 = ""

lower = sorted([ch for ch in s if ch.islower()])
upper = sorted([ch for ch in s if ch.isupper()])
odd = sorted([ch for ch in s if ch.isdigit() and int(ch) % 2 != 0])
even = sorted([ch for ch in s if ch.isdigit() and int(ch) % 2 == 0])
str1 = "".join(lower+upper+odd+even)
print(str1)