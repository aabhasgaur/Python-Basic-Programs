import sys

# Linked list node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def push(head, data):
    if not head:
        return Node(data)

    # Allocate dynamic memory for newNode.Assign the data into newNode.
    newNode = Node(data)

    # newNode.next assign the address of head node.
    newNode.next = head

    # newNode become the headNode.
    head = newNode
    return head

# Function that convert singly linked list into circular linked list.
def circular(head):

    # declare a node variable start and assign head node into start node.
    start = head

    # check that while head.next not equal to null then head points to next node.
    while(head.next is not None):
        head = head.next

    # if head.next points to null then start assign to the head.next node.
    head.next = start
    return start

# Function that display the elements of circular linked list.
def displayList(node):
    start = node
    while(node.next is not start):
        print("{} ".format(node.data),end="")
        node=node.next

    # Display the last node of circular linked list.
    print("{} ".format(node.data),end="")

# Driver Code
if __name__=='__main__':

    # Start with empty list
    head=None

    # Using push() function to convert singly linked list 17.22.13.14.15
    head=push(head,15)
    head=push(head,14)
    head=push(head,13)
    head=push(head,22)
    head=push(head,17)

    # Call the circular_list function that converst singly linked list to circular linked list.
    circular(head)
    print("Display List:")
    displayList(head)
