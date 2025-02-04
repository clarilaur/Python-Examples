fruits = {
    "apple": 2.5,
    "banana": 1.2,
    "grape": 3.0,
    "orange": 1.8
}

total = 0
while True:
    requests = input('insert:').lower()

    if requests == 'done':
        break

    value = fruits.get(requests)

    total += value

print(total)
