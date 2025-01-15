one = input()
two = input()

words_one = one.split()
words_two = two.split()

for word1, word2 in zip(words_one,words_two):
    if word1 != word2:
        print(word1, word2)
