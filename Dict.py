# dictionary: key-value pairs, unordered, mutable

mydict = {"name": "keely", "age": 19, "city": "Kingston"}
print(mydict)

if "name" in mydict:
    print(mydict["name"])

mydict.pop("age")
print(mydict)

# iterate over
for key in mydict:
    print(key)

for value in mydict:
    print(value)

mydict_cpy = mydict.copy()
print(mydict_cpy)

