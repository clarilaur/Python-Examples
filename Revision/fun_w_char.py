def check_character(word, index):
    char = word[index]
    if char.isdigit():
        return (f"Character '{char}' is a digit")
    elif char.isalpha():
        return (f"Character '{char}' is a letter")
    elif char.isspace():
        return (f"Character '{char}' is a white space")
    else:
        return (f"Character '{char}' is unknown")   
  
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
