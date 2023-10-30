'''Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3'''
class TreeNode:
    def __init__(self,key):
        self.key =key
        self.val = None
        self.right = None
        self.left = None

# def max_d(curr):
#     if curr is None:
#         return 0
    

def maximum_depth(root):
    if root is None:
        return 0
    right = maximum_depth(root.right)
    left = maximum_depth(root.left)
    return 1+max(right, left)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maximum_depth(root))
