def count_wordfreq(filename):
    try:
        freq = {}
        with open(filename) as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.upper().strip(',.!?')
                    freq[word] = freq.get(word, 0) + 1
            return freq

    except FileNotFoundError:
        print("File Not Found!")
        return {}

result = count_wordfreq("Demo.txt")
print(result)
for key, value in result.items():
    print(f"{key}:{value}")