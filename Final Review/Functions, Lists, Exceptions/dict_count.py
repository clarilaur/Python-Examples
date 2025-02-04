sentence = input('insert:')

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, value in word_count.items():
    print(f'{word}: {value}')
