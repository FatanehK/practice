"""Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/"""
from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def getMinimumDifference(root) -> int:
    prev = None
    result = float("inf")

    def dfs(node):
        nonlocal prev, result
        if not node:
            return
        dfs(node.left)
        if prev:
            result = min(result, abs(node.val - prev.val))
        prev = node
        dfs(node.right)

    dfs(root)
    return result


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
# [4,2,6,1,3]
print(getMinimumDifference(root))
