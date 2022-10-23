import matplotlib.pyplot as plt
def calculate():
    y  =  [1, 4, 9]
    
    lst = list(range(4,101))
    term = len(y) + 1

    for num in lst:
        value = (y[-1]) - (y[-2]) + (y[-3]) + 2*(2*term-3)
        y.append(value)
        term += 1
    print(y)

    x = list(range(1,101))

    plt.plot(x,y)
    plt.xlabel('Terms from 1-100')
    plt.ylabel("Values")
    plt.title("Question 7")

    plt.show()



calculate()



