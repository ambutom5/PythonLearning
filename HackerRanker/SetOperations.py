# One set has subscribed to the English newspaper, and
# one set has subscribed to the French newspaper.
# Your task is to find the total number of students who
# have subscribed to only English newspapers.

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
c = a-b
print(c)
print(len(c))