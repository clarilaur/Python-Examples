#import pigAge module and call pigAge_converter()
import pigAge
#one pig year is equivalent to five human years

#solution accepts integer input representing a pig's age
pig_age = int(input())
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")
convert = pigAge.pigAge_converter(pig_age)
print(f'{pig_age} is {convert} in human years')
