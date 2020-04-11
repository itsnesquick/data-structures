#!/usr/bin/env python

__author__ = "Maximilian Niquet"
__credits__ = ["Maximilian Niquet"]
__license__ = "MIT"
__version__ = "0.0.1"
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

    def __init__(self):
        self.head = None

    def push(self):
        """
        Description: Inserts given element at the end of the linked list
        """
        pass

    def delete(self):
        """
        Description: Deletes given element from the linked list
        """
        pass

    def unshift(self):
        """
        Description: Deletes the first element of the linked list
        """
        pass

    def shift(self):
        """
        Description: Inserts given element at the head of the linked list
        """
        pass

    def search(self):
        """
        Description: Returns the given element from linked list
        """
        pass

    def isEmpty(self):
        """
        Description: Returns if the linked list is empty
        """
        pass