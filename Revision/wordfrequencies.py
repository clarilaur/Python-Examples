
def build_dictionary(words):
    dictionary = {}  
    
    for word in words:
        if word in dictionary:  
            dictionary[word] += 1 
        else:
            dictionary[word] = 1  
    
    return dictionary


if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))
