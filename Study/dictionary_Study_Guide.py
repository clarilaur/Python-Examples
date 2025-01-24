student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key)



capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}


print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic.keys())

print(soundtrack_dic.values())

album_sales_dict = {"Back in Black": "50 Million", "The Bodyguard":"50 Million", "Thriller":"65 Million"}
print(album_sales_dict)

print(album_sales_dict["Thriller"])
print(album_sales_dict.keys())
print(album_sales_dict.values())
