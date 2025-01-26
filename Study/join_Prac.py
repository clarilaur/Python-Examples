#Using join() with Dictionary

given = {'Geek': 1, 'for': 2, 'Geeks': 3}

givens = ' '.join(given)
print(givens)

#Join with Loop for Custom Formatting
given = ["apple", "banana", "cherry"]

givens = '('+'), ('.join(given)+')'
print(givens)

#Using join()
given = ["apple", "banana", "cherry"]
givens= []
for item in given:
    givens.append(item.upper())
g = ' '.join(givens)
print(g)
