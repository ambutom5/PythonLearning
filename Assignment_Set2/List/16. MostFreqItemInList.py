list1 = ["Apple","Banana","Apple","Apple","Guava"]
freq = {}

for i in list1:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

for key,value in freq.items():
    print(key,":",value)

maxc = secmaxc = 0
maxw = secmaxw = None

for word in freq:
    if freq[word]>maxc:
        secmaxc = maxc
        secmaxw = maxw
        maxc = freq[word]
        maxw = word
    elif freq[word]>secmaxc and freq[word]!=maxc:
        secmaxc = freq[word]
        secmaxw = word

print()
print(maxw,":",maxc)
print(secmaxw,":",secmaxc)


# freq = {}
#
# for item in list1:
#     freq[item] = freq.get(item,0)+1
# print(freq)
#
# sorted = sorted(freq.items(),key = lambda x:x[1],reverse=True)
# print(sorted)
#
# print(f"Most Frequent Word: {sorted[0][0]}, occuring {sorted[0][1]} times")
