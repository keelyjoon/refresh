def calculate():
    my_list  =  [1, 4, 9]
    
    lst = list(range(4,101))
    term = len(my_list) + 1

    for num in lst:
        value = (my_list[-1]) - (my_list[-2]) + (my_list[-3]) + 2*(2*term-3)
        my_list.append(value)
        term += 1
    print(my_list)

calculate()



