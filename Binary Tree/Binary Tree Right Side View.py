"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            right_side = None
            len_q = len(q)
            for i in range(len_q):
                curr = q.popleft()
                if curr:
                    right_side = curr
                    q.append(curr.left)
                    q.append(curr.right)

            if right_side:
                result.append(right_side.val)
        return result


root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)


p = root.left
q = root.left.left
sol = Solution()
print(sol.rightSideView())
