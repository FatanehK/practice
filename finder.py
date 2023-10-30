'''
We are interested in writing a function to compare a given search value to a binary search tree. Specifically, we want to know whether the search value is smaller, bigger, or spanned by the tree.

Our function should accept two arguments, the root of a tree, and a search value to compare against it. The ouput of our functions should be as follows:

- If the value is smaller than the smallest element in the tree, our function should return 'smaller'
- If the value is larger than the largest element in the tree, our function should return 'larger'
- If the value is between the smallest and largest element (inclusive) in the tree, our function should return 'spanned'

For example, given this tree:

           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9

If the search value was 10, our function should return 'bigger', because 10 is greater than 9.
If the search value was 0, our function should return 'smaller', because 0 is less than 1.
If the search value was 4, our function should return 'spanned', because 4 is between 1 and 9 (inclusive).
If the search value was 1, our function should return 'spanned', because 1 is between 1 and 9 (inclusive).
'''

# DO NOT MODIFY THE NODE CLASS
from collections import deque


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compare(tree, search_value):
    visited =[]
    min_val = float('inf')
    max_val = float('-inf')
    if tree is None:
        return 0
    queue = deque([tree])
    while queue:
        curr= queue.popleft()
        if curr.value < min_val:
            min_val = curr.value
        elif curr.value > max_val:
            max_val = curr.value
        if curr not in visited:
            visited.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    if search_value < min_val:
        return "smaller"
    elif search_value > max_val:
        return "bigger"

    elif search_value >= min_val and search_value <= max_val:
        return "spanned"


# def compare(tree, search_value):
#     min_val = float("inf")
#     max_val = float("-inf")
#     if tree is None:
#         return 0
#     queue = deque([tree])
#     visited = [tree]
#     while queue:
#         curr = queue.popleft()
#         if curr.value < min_val:
#             min_val = curr.value
#         elif curr.value > max_val:
#             max_val = curr.value
#         if curr.left:
#             if curr.left not in visited:
#                 if curr.value <= min_val:
#                     min_val = curr.value
#                     queue.append(curr.left)

#         if curr.right:
#             if curr.right not in visited:
#                 if curr.value >= max_val:
#                     max_val = curr.value
#                     queue.append(curr.right)
#             # print(max_val)

#     if search_value < min_val:
#         return "smaller"
#     if search_value > max_val:
#         return "bigger"
#     if search_value >= min_val and search_value <= max_val:
#         return "spanned"


'''
           6
         /   \
        /     \
       3       8
      / \       \
     1   5       9
'''
tree = Node(6, Node(3, Node(1), Node(5)), Node(8, None, Node(9)))
assert compare(tree, 10) == "bigger"
assert compare(tree, 0) == "smaller"
assert compare(tree, 4) == "spanned"
assert compare(tree, 1) == "spanned"
assert compare(tree, 5) == "spanned"
assert compare(tree, 9) == "spanned"


'''
           5
         /   \
        /     \
       3       7
      /         \
     1           8
    /             
   0               
'''
tree = Node(5, Node(3, Node(1, Node(0))), Node(7, None, Node(8)))
assert compare(tree, 9) == "bigger"
assert compare(tree, -1) == "smaller"
assert compare(tree, 0) == "spanned"
assert compare(tree, 8) == "spanned"


print("All tests passed! Discuss time & space complexity if time remains")
