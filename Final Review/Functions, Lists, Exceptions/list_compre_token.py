sentence = input('insert:')

tokens = sentence.split()

process = [token.upper() + '_A' if 'a' in token else token.upper() for token in tokens]

print(process)
