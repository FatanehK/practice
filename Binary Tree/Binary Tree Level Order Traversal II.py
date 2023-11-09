'''Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []'''
from collections import deque
class Node:
    def __init__(self,val):

        self.val=val
        self.right= None
        self.left = None
class Solution:
    def levelOrderBottom(self, root):

        result =[]
        queue = deque([root])
        while queue:
            level=[]
            len_q= len(queue)
            for _ in range(len_q):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.insert(0,level)
        return result
sol = Solution()
root =Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.right = Node(7)   
root.right.left = Node(15)  
print(sol.levelOrderBottom(root))