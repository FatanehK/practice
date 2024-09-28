"""Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    if not root:
        return []
    result = []

    def dfs(node, path):
        if not node:
            return
        path = path + str(node.val)
        # path = path + [node.val]
        if not node.left and not node.right:
            result.append(path)
        else:
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

    # dfs(root,[])
    dfs(root, "")
    return result


root = TreeNode(3)
root.left = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
print(binaryTreePaths(root))
