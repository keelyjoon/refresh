"""
Remove duplicates from an array
"""
from tkinter import E


def duplicatesArray(listy):
    new_array = []
    duplicates_array = []
    for item in listy:
        if item not in new_array:
            new_array.append(item)
        else:
            duplicates_array.append(item)
    print(new_array)

#duplicatesArray([1, 2, 2, 3, 3, 3, 2, 1, 5, 5, 4, 6, 7])

"""
Sort an unordered array of objects
"""
def sortArray(listy):
    listy.sort()
    print(listy)

#sortArray(["hello", "my", "name", "is", "keely", "joon"])

"""
two sorted arrays into a thrid sorted array
"""
def sortedArrays(list1, list2):
    print("this is list1: ", list1)
    print("this is list2: ", list2)
    list1.extend(list2)
    list1.sort()
    print("this is the combind sorted list:", list1)
#sortedArrays([1,2,3,4,5], [3,4,5,6,7,8,9])

"""
Given an infinitely long sorted array of numbers,
write a program that will determine if a given number is in the array
"""
def isInArray(list, target):
    if target in list:
        print("true")
    else:
        print("false")

#isInArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 9)

"""
Write a program that will find all the prime numbers in array
"""
def primeNums(num):
    # first, the conditional to make sure the num is greater than 1
    if num > 1:
        # a loop that iterates through the range
        for i in range(2, int(num/2) + 1):
            # checking to see if the number is divisable by itself
            if num % i == 0:
                print(num, " is not a prime number")
                break
        else:
            print(num, " is a prime number")
    else:
        print(num, " is not a prime number")
#primeNums(12)

"""
Write a function that takes in an array of integers
and returns the duplicates and the number of times
they were found.
"""
def duppyArray(listy):
    duplicates = {}
    for item in listy:
        if item in duplicates.keys():
            duplicates[item] += 1
        else:
            duplicates[item] = 1
    
    for key, value in enumerate(duplicates.values()):
        if value > 1:
            print("the number: ", key+1, "appears ", value, " times")
    
duppyArray([1, 2, 3, 4, 5, 5, 5, 5, 6, 69, 69])


