file_name = input()

with open(file_name,'r') as file:
    lines = file.readlines()
    
    categories = []
    names = []
    descriptions = []
    availabilities = []
    
    for l in lines:
       parts = l.strip().split('\t')
       if len(parts) == 4:
           category, name, description, availability = parts
           categories.append(category)
           names.append(name)
           descriptions.append(description)
           availabilities.append(availability)
           
    for i in range(len(names)):
        if availabilities[i]== 'Available':
