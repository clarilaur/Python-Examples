various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

index_value = int(input())


index = various_data_types[index_value]


data_type = type(index).__name__
print(f'Element {index_value}: {data_type}')
