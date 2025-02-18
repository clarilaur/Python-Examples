def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        st = st.replace(vowel, "!")
    return st


result = replace_exclamation('aeiouAEIOU')
print(result)
