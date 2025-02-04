people = [
    {"name": "Alice", "age": 30, "height": 5.7},
    {"name": "Bob", "age": 25, "height": 6.1},
    {"name": "Charlie", "age": 35, "height": 5.9}
]

for person in people:
    name = person['name']
    age = str(person['age'])
    height = str(person['height'])
    print(f'Name: {name}, Age: {age}, Height: {height}')
