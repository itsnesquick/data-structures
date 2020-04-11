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