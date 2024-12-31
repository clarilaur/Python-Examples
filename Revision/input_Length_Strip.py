user_text = input()

update = user_text.replace(",", "").replace(".", "").replace(" ", "").replace("!", "")
numcha = len(update)
print(numcha)
