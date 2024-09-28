"""Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, targetSum):
    if not root:
        return []
    result = []

    def dfs(node, currSum, path):
        if not node:
            return 0

        currSum += node.val
        new_path = path + [node.val]
        if not node.left and not node.right:
            if currSum == targetSum:
                result.append(new_path)

        else:
            dfs(node.left, currSum, new_path)
            dfs(node.right, currSum, new_path)

    dfs(root, 0, [])
    return result


root = TreeNode(3)
root.left = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
print(path_sum(root, 11))
