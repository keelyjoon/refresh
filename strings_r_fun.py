'''
split a string into a list without using split method
'''
def split_string(string):
    split_value = []
    tmp = ''
    for c in string:
        if c == ' ':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    
    print(split_value)

#split_string("this is a sentence")

'''
- Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the
input string is valid.
'''
def isValid(s):
    while "()" in s and "{}" in s and "[]" in s:
        s = s.replace("()", "").replace("{}", "").replace("[]","")
        print(s == "")
    
#isValid("(){}{}[]")

"""
Create function to return if a string a palindrome
"""
def isPalindrome(string):
    # convert string to uppercase
    string_upper = string.upper()
    # compare string to reversed string 
    print(string_upper == string_upper[::-1])
#isPalindrome("appleelppa")

"""
reverse a given string
"""
def reverse(string):
    reversed_string = string[::-1]
    print(reversed_string)
#reverse("apple")

"""
a function to find a certain string within a string
"""
def inString(string, substring):
    if substring in string:
        print("true")
    else:
        print("the substring: ", substring, "is not in the string: ", string)
#inString("hello", "elleo")

"""
a function that gives a string and a reversed string and compares the two
"""
def compareReverse(string, reversedString):
    if string[::-1] == reversedString:
        print("true")
    else:
        print("false")
#compareReverse("hello", "holleh")