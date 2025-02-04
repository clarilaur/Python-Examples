data = [10, 3.14, "hello", 5, 2.71, "world"]

for item in data:
    item_type = type(item).__name__  # Get the type of the item as a string
    print(f'{item} (converted from {item_type})')
