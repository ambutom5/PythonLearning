n = int(input())
list1 = list(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

sym_diff = set(list1) ^ set(list2)

for i in sorted(sym_diff):
    print(i)

