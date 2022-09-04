# Lists: ordered, mutable, allows duplicate elements
my_list = ["banana", "cherry", "apple"]
print(my_list)

# make a new list using the list function (empty list)
my_list2 = list()
print(my_list2)

# indexing 
item = my_list[2]
print(item)

# iterating over lists
for i in my_list:
    print(i)

# check to see if an element is in a list
if "banana" in my_list:
    print("yes")
else:
    print("no")

# adding item to the end
my_list.append("lemon")
print(my_list)

# removing items 
thing = my_list.pop()
print(thing)

# sorts a list in acesending order
new_list = [3,6,3,6,8,9,3,1,5]
print(new_list)

# this makes a new list that is sorted
sorted_list = sorted(new_list)
print(sorted_list)

# this changes the original list
changes = new_list.sort()
print(new_list)

# makes a list with repeating items
zero_list = [0] * 5
print(zero_list)

# add two lists together 
adding_list1 = [1,2,3]
adding_list2 = [4,5,6]
added_list = adding_list1 + adding_list2
print(added_list)

#slicing
slice_list = [1,2,3,4,5,6,7,8,9]
# start at index 1 end at index 5
a = slice_list[1:5]
print(a)
# if you don't specifiy a start it starts at index 0

# list comprehension
og_list = [1,2,3,4,5,6]
# creates a list with squared numbers of the og_list
b = [i*i for i in og_list]
print(og_list)
print(b)