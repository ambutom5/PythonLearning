# Output the total number of distinct country stamps on a single line.

# Sample Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France

# Sample Output
# 5

n = int(input())
countries = set()
for _ in range(n):
    country = input().strip()
    countries.add(country)
print(len(countries))