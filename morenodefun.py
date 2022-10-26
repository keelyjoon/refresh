"""
This file contains a Node and LinkedList class to create a linkedList and traverse
through the list llist
"""
# this is our node class
class Node:
    # this is our constructor for our node class
    def __init__(self, data):
        # this varaible is for the node data
        self.data = data
        # this varaible is for the node link
            # set node link to none to start
        self.link = None

# this is our likedList class
class LinkedList:
    # this is our constrcutor for our LinkedList class
    def __init__(self):
        # this variable is to initalize our head node
        self.head = None

    # this method is to print our linked List
    def printList(self):
        # this is our temp varaible which we will set to our head node
            # we do this because once we have our head node, we can print the things
            # that are linked to it
        temp = self.head

        # for loop to iterate through the linked list as it has a pointer
        while(temp):
            # print the current (temp) varaible's data
            print(temp.data)
            # update the temp varaible to the next node (link)
            temp = temp.link

# main method for creating the nodes and linked list
if __name__ == "__main__":
    # create an empty linked list using the linkedList class
    llist = LinkedList()

    # create a head node for the linkedList using node class
    llist.head = Node("this will be our head node")
    # create second node
    second = Node("this will be our second node")
    # link head node to second node
    llist.head.link = second
    # create third node
    third = Node("this will be our third node")
    # link second node to third node
    second.link = third

    # since we are only creating three nodes, we don't link the third node to 
    # anything, thus it is linked to null

    # print the linked list by calling our printList method 
    llist.printList()

