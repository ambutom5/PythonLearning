# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


x, y, z, n = 1, 1, 1, 2
result = [[i, j, k]
          for i in range(x+1)   # i goes 0 → x
          for j in range(y+1)   # j goes 0 → y
          for k in range(z+1)   # k goes 0 → z
          if i + j + k != n]
print(result)

