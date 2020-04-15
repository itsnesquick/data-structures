#!/usr/bin/env python

__author__ = "Maximilian Niquet"
__credits__ = ["Maximilian Niquet"]
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "Maximilian Niqiet"
__email__ = ""
__status__ = "Development"

"""
Filename: linked_list.py
Description: 
"""

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        """
        Description: Inserts given element at the end of the linked list
        """
        end = Node(data)
        n = self.head
        while(n.next != None):
            n = n.next
        n.next = end

    def delete(self, data):
        """
        Description: Deletes given element from the linked list
        """
        n = self.head
        while(n.next != None):
            if(n.next.data == data):
                n.next = n.next.next
                return True
            else:
                n = n.next
        return False

    def unshift(self):
        """
        Description: Deletes the first element of the linked list
        """
        n = self.head
        if n.next is None:
            self.head = Node()
        else:
            self.head = n.next
        n.next = None
        return n

    def shift(self, data):
        """
        Description: Inserts given element at the head of the linked list
        """
        n = self.head
        self.head = Node(data)
        self.head.next = n

    def search(self):
        """
        Description: Returns the given element from linked list
        """
        pass

    def isEmpty(self):
        """
        Description: Returns if the linked list is empty
        """
        if self.head != None:
            return False
        else:
            return True

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current is not None:
                print(" -> ", end="")
            current = current.next
    
if __name__ == "__main__":
    
    linked_list = LinkedList(4)

    linked_list.push(6)
    linked_list.push(14)
    linked_list.push(7)
    linked_list.push(1)
    linked_list.push(3)
    print(end="\n")
    
    print(linked_list.printList())
    print(end="\n")
    
    print(linked_list.delete(3))
    print(end="\n")
    
    print(linked_list.printList())
    print(end="\n")

    rem = linked_list.unshift()
    print(rem.data, "->", rem.next)
    print(end="\n")

    rem_2 = linked_list.unshift()
    print(rem_2.data, "->", rem_2.next)
    print(end="\n")

    print(linked_list.printList())
    print(end="\n")

    linked_list.shift(23)

    print(linked_list.printList())
    print(end="\n")