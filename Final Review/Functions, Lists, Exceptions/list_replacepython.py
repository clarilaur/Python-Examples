enter = input('insert:')

replace_py = enter.replace('Python','🐍 Python')

for i in ['.', ',', '!', '?', ';', ':']:
    replace_py = replace_py.replace(i, ' ')

cleaned_text = ' '.join(replace_py.split())
print(cleaned_text)
