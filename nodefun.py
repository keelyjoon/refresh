class Node:
    # constructor 
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# create nodes  
e1 = Node('Mon')
e2 = Node('Wed')
e3 = Node('Tue')
e4 = Node('Thu')

# linking nodes together  
e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

    # e4 points to null

# e1 --> e3 --> e2 --> e4 --> null

thisvalue = e1
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval