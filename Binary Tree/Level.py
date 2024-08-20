"""
We are interested in writing a function that returns which level in 
a binary tree has the most nodes. The root of the tree is considered level 0. 

Our function should accept one argument, the root of the binary tree and return an integer representing the level of the tree with the most nodes. 

For example, given the root of this tree:

Level 0:             1
                   /    \
                  /      \
Level 1:         2        3
               /   \    /   \
Level 2:      4     5  6     7
             / \      /     
Level 3:    8   9    10 

The function should return 2 because level 2 has 4 nodes (4, 5, 6, 7) which is more than any of the other levels.

If the tree is empty, return -1. 
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_Binary_tree(root):
    q = deque([root])
    max_level = 0
    max_len_q = 0
    level = 0

    while q:
        len_q = len(q)
        if len_q > max_len_q:
            max_len_q = max(max_len_q, len_q)
            max_level = level
        for _ in range(len_q):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        level += 1
    return max_level


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
assert max_level_Binary_tree(root) == 2
