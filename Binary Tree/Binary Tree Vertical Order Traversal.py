"""Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
from collections import deque, defaultdict


def vertical_order_traversal_binary_tree(root):
    if not root:
        return []
    map_tree = defaultdict(list)
    q = deque([[root, 0]])
    min_col = float("inf")
    max_col = float("-inf")
    result =[]
    while q:
        curr, col = q.popleft()
        if col < min_col:
            min_col = col
        elif col > max_col:
            max_col = col
        map_tree[col].append(curr.val)
        if curr.left:
            q.append([curr.left, col - 1])
        if curr.right:
            q.append([curr.right, col + 1])
    for col in range(min_col, max_col + 1):
        result.append(map_tree[col])
    return result


root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(vertical_order_traversal_binary_tree(root1))
