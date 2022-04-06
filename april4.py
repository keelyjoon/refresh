# Given two strings n and m, return true if they are equal when both
# are entered into text editors. But: a # means a backspace character 
# (deleting backwards), and a % means a delete character (deleting forwards).

import numpy as np

def equalsWithDeletions(n, m):
    # makes an array of each char in n
    n_list = [i for i in n]
    # makes an array of each char in m
    m_list = [i for i in m]
    listMaker(n_list)
    listMaker(m_list)
 

def listMaker(list):
    count = 0
    # while the length of the list is greater than count 
    while len(list) > count:
        # if the list at the count index = #...
        if list[count] == '#':
            # make the list at index count equal to an empty string
            list[count] = ' '
            # if count is greater than zero
            if count > 0:
                # make the list at index count-1 equal to an empty string
                list[count-1] = ' '
                # increase count
                count+=1
            # otherwise...increase count without doing the above
            else:
                count+=1
        # elif the list at index count equals %
        elif list[count] == '%':
            # make the list at index count equal an empty string
            list[count] = ' '
            # if count plus 1 is equal to the length of the list
            if count + 1 == len(list):
                # add one to count without doing anything else
                count+=1
            # otherwise..
            else:
                # make the list at index count + 1 equal an empty string
                list[count+1] = ' '
                # add one to count
                count+=1
        # otherwise just add one to count
        else:
            count+=1 
    # call deleteSpaces method with the list
    deleteSpaces(list)

def deleteSpaces(list):
    # make an empty list
    new_list = []
    for string in list:
        # if the original list at each index is not equal to an empty string
        if string != " ":
            # add the value to the new list
            new_list.append(string)
    
    # turn list into string
    final_string = "".join(str(word) for word in new_list)

    # print the final string
    print(final_string)


equalsWithDeletions("Ke#eel%yy_Mc#c#cSp%uurre#en", "Keely_McSpurren")