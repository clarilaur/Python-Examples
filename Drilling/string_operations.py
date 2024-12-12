pups = 'Rio and Pippy are the best dogs in the whole world'

print(len(pups))
print(pups.title()) #capitalizes all first letters
print(pups.lower()) #lowers all first letters

print(pups.count('i')) #counts how many times the value appears


print(pups[0:5]) #slicing

pup1 = 'Rio'
pup2 = 'Pippy'

message = "{} and {} are my angel babies.".format(pup1,pup2)
print(message)

listmessage = message.split(' ') #splits, returns a list
print(listmessage)
