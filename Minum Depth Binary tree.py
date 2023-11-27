'''111. Minimum Depth of Binary Tree
Easy
5.8K
1.1K
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the 
root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000'''

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.val = None
        self.right = None
        self.left = None

# def min_tree(root):
#     if root is None:
#         return 0

    # left_depth = min_tree(root.left)
    # right_depth = min_tree(root.right)

    # if root.left is None or root.right is None:
    #     return max(left_depth, right_depth) + 1

    # return min(left_depth, right_depth) + 1
    # queue= deque([{"node":root,"level":1}])
    # while queue:
    #     curr = queue.popleft()
    #     node = curr["node"]
    #     level = curr["level"]
    #     if node.left is None and node.right is None:
    #         return level
    #     if node.left:
    #         queue.append({"node": node.left, "level": level+1})
    #     if node.right:
    #         queue.append({"node": node.right, "level": level+1})

    # if root.left and root.right:
    #     return min(min_tree(root.left), min_tree(root.right))+1
    # else:
    #     return min_tree(root.left or root.right)+1

def binary_tree_level(root):
    if root is None:
        return 0
    result=[]
    queue = deque([root])
    while queue:
        level =[]
        len_q= len(queue)
        for _ in range(len_q):
            curr = queue.popleft()
            level.append(curr.key)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        result.append(level)
    return result



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right= TreeNode(7)
# print(min_tree(root))
print(binary_tree_level(root))
