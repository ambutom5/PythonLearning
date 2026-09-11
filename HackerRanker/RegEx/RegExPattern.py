# Sample Input
# # 100,000,000.000

# Sample Output
# 100
# 000
# 000
# 000

import re

pattern = "100,000,000.000"
print("\n".join(re.split("[,.]",pattern)))

print()
print()

regp = pattern.replace(",","").replace(".","")
print(regp)

for i in range(0,len(regp),3):
    print(regp[i:i+3])