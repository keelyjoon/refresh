# Given two strings n and m, return true if they are equal when both
# are entered into text editors. But: a # means a backspace character 
# (deleting backwards), and a % means a delete character (deleting forwards).

import numpy as np

def equalsWithDeletions(n, m):
    # makes an array of each char in n
    n_list = list(n.split(" "))
    # makes an array of each char in m
    m_list = list(m.split(" "))
    listMaker(n_list)
    listMaker(m_list)
 

def listMaker(list):
    count = 0
    while len(list) > count:
        if list[count] == '#':
            list[count] = ' '
            if count > 0:
                list[count-1] = ' '
                count+=1
            else:
                count+=1
        elif list[count] == '%':
            list[count] = ' '
            if count + 1 == len(list):
                count+=1
            else:
                list[count+1] = ' '
                count+=1
        else:
            count+=1 
    print(list)
    #deleteSpaces(list)

def deleteSpaces(list):
    test_list = [i for i in list if i]
    print(test_list)


equalsWithDeletions("k#eely j%on", "eelyjn")
