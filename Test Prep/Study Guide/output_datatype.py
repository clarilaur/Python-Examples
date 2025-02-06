various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

index_value = int(input())

location = various_data_types[index_value]
data_type = type(location).__name__

print(f'Element {index_value}: {data_type}')
