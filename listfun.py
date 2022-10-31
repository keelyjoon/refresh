# create an empty list 
listy = []

# add elements to list 
new_element = 5
listy.append(new_element)

# print list
print("this is the list", listy)

# add more elements to list 
listy.append(27)
listy.append(15)
listy.append(12)
listy.append(6)

print("this is the updated list: ", listy)

# sort list 
listy.sort()
print("this is the sorted list", listy)

# reverse list 
listy.reverse()
print("this is the revered list", listy)

# add duplicates to list
listy.append(27)
listy.append(15)
listy.append(25)
listy.append(6)
print("this is the updated list", listy)

# swap first and last elements of the list
temp = listy[0]
listy[0] = listy[-1]
listy[-1] = temp
print("swapped the first and last element of the list", listy)

# Find the length of a list
print("the length of the list is", len(listy))

# count the occurence of a number in a list
count = 0
for item in listy:
    if item == 27:
        count += 1
print("the number of 27's in listy is: ", count)

# multiply all the items in the list by 
listy_multiply = []
for item in listy:
    new_item = item * item 
    listy_multiply.append(new_item)
print("the multiplied list is: ", listy_multiply)

# even numebrs in list
even_listy = []
odd_listy = []
for item in listy:
    if item % 2 == 0:
        even_listy.append(item)
    else:
        odd_listy.append(item)
print("these are the even numbers", even_listy)
print("these are the odd numbers", odd_listy)

# largest number in the list 
largest_num = listy[0]
for item in listy:
    if largest_num < item:
        largest_num = item
print("this is the largest number", largest_num)

# print duplicates 
duplicate_list = []
new_list = []
for item in listy:
    if item not in new_list:
        new_list.append(item)
    else:
        duplicate_list.append(item)
print("these are the duplicate elemnts", duplicate_list)

# remove duplicates
li = [3, 2, 2, 1, 1, 1]
print("here we have removed the duplicates", list(set(li)))

# append vs extend
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

list_a.extend(list_b)
print(list_a)

# deleting methods from lists
del list_a[0]
print("deleted the element at index 0 of the list", list_a)

list_a.pop(0)
print("popped the first element off of the list", list_a)

# find the index of a value
print("this is the value of index 6: ", list_a.index(6))

# iterate through list and print the index and value
grocery_list = ['flour','cheese','carrots']
for idx,val in enumerate(grocery_list):
    print("%s: %s" % (idx, val))

first_list = [25, 44, 76, 69]
print(first_list)
first_list.sort()
print(first_list)
first_list.sort(reverse=True)
print(first_list)
