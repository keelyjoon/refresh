# Tuple: ordered, imutable, allows duplicate elements
my_tuple1 = ("keely", 19, 'cool')
print(my_tuple1)
# to find the type of a varaible, use the type method
print(type(my_tuple1))

# access items
item = my_tuple1[1]
print(item)

# YOU CANT CHANGE TUPLES, they are imutable

# index
print(my_tuple1.index("keely"))

# slicing 
a = (1,2,3,4,5,6,7,8,9)
b = a[2:5]
print(a)
print(b)
# to reverse tuple 
c = a[::-1]
print(c)

# unpacking tuple 
test_tuple = "keely", 19, "Toronto"
name, age, city = test_tuple
print(name, age, city)