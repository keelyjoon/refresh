"""
this is a file that will use the node and linked list class to traverse a linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.link 

    # using to pointers curr and prev
    def reverse_list(self,head):
        # initalize pointers 
        prev, curr = None, head
        # keep going until end of linked list
        while curr:
            # temp varaible
            nxt = curr.link
            curr.link = prev
            prev = curr
            curr = nxt
        return prev


if __name__ == "__main__":

    llist = LinkedList()

    llist.head = Node("first node")
    second = Node("second node")
    third = Node("third node")

    llist.head.link = second
    second.link = third
    
llist.printList()