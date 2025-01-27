word = input()
if len(word) == 3:
    midfix = len(word) // 3  # Find one-third of the length
    result = word[0:midfix+3]  # Slice the word from midfix to midfix+3 (for 3 characters)

    print(f'Midfix: {result}')
else:
    midfix = len(word) // 2  # Find one-third of the length
    result = word[midfix-1:midfix+2]  # Slice the word from midfix to midfix+3 (for 3 characters)

    print(f'Midfix: {result}')
