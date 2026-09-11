s = "qA2"

print(any(ch.isalpha for ch in s))
print(any(ch.isdigit() for ch in s))
print(any(ch.isupper() for ch in s))
print(any(ch.islower() for ch in s))
print(any(ch.isnumeric() for ch in s))
print(any(ch.isalnum() for ch in s))
print(any(ch.isspace() for ch in s))

print()

print(all(ch.isalpha for ch in s))
print(all(ch.isdigit() for ch in s))
print(all(ch.isupper() for ch in s))
print(all(ch.islower() for ch in s))
print(all(ch.isnumeric() for ch in s))
print(all(ch.isalnum() for ch in s))
print(all(ch.isspace() for ch in s))

# any(c.isalnum() for c in s) → True if at least one character is alphanumeric.
# all(c.isalnum() for c in s) → True if every single character is alphanumeric.