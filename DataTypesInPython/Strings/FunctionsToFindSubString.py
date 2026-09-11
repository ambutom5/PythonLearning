string = ("Introduction to Python Programming, "
          "Python is simple and easy to use and learn.")

print(string)
print(string.find("to"))                    # returns the first occurrence
print(string.find("Luminar"))

print(string.index("to"))
print(string.index("Introduction"))
# print(string.index("Luminar"))            # ValueError: substring not found

print(string.rfind("to"))                   # returns the last occurrence
print(string.rfind("Introduction"))

print(string.count("to"))
print(string.count("Introduction"))
print(string.count("o"))


