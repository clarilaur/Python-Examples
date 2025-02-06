filename = input()

with open(filename, 'r') as file:
    words = file.readlines()
    if len(words) == 3:
      #learn this part
        words = [word.strip() for word in words]
        sentence = ' '.join(words)
with open(filename, 'a') as file:
    file.write(f"\n{sentence}")
with open(filename, 'r') as file:
    contents = file.read()
    print(contents)
