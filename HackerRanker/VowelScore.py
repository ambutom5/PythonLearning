# The score of a single word is 2 if the word contains an even number of vowels.
# Otherwise, the score of this word is 1.
# The score for the whole list of words is the sum of scores of all words in the list.

sentence = "programming is awesome"
words = sentence.split()
score = 0
for word in words:
    count = 0
    for char in word:
        if char in 'aeiouAEIOU':
            count += 1
    if count % 2 == 0:
        score += 2
    else:
        score += 1
print(score)
