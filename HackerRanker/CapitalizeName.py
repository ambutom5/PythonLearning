s = "hello   world"
print(" ".join(word.capitalize() for word in s.split(' ')))


# split(' ') ensures you don’t lose the original spacing when rejoining.
# split() → splits on any whitespace and collapses consecutive spaces into one.