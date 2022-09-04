# strings: ordered, immutable, text representation

# how to make the variable 
my_string = "Hello world"
multi_string = """hello 
world"""

# acess a char 
char = my_string[0]
print(char)
# you can't change the letters in a string because they are immutable 

# splicing strings
substing = my_string[1:5]
print(substing)

# to reverse a string 
reverse_string = my_string[::-1]
print(reverse_string)

# iterating over string 
greeting = "hey there"
for x in greeting:
    print(x)

# checking for chars or substrings in strings
if 'ell' in greeting:
    print("yes")
else:
    print("no")

