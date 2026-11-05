n = 12321
s = 0
temp = n

while n > 0:
    digit = n % 10
    s = s + digit
    n = n // 10

if s == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
