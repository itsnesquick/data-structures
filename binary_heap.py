#!/usr/bin/env python

__author__ = "Maximilian Niquet"
__credits__ = ["Maximilian Niquet"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Maximilian Niqiet"
__email__ = ""
__status__ = "Development"

"""
Filename: binary_heap.py

Description: 

Binary Heap is a Binary Tree which is:

1) a complete tree (usually represented as an array),
2) either a Min Heap (key at root must be minimum among all
   keys present in the tree) or a Max Heap (key is maximum).

- The root element will be Array[0]
- Example for ith node, Array[i]:
    - Array[(i - 1) / 2] returns the parent node
    - Array[(2 * i) + 1] returns the left child node
    - Array[(2 * i) + 2] returns the right child node

"""

