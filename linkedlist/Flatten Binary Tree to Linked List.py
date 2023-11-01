'''Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right=None
        self.left =None

def flatten(root):
    """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
    """
    # Flatten the root tree and return tail
    def dfs(root):
        if not root:
            return None
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)
        # if both of them is empty we don't need to do anything 

        # if rightside is empty we have to take the leftTail and move it to the right side

        # if not left we don't need to do anything 

        if leftTail:
            leftTail.right = root.right #attach to righside
            root.right = root.left# root at the beginig of leftside
            root.left = None

        last= rightTail or leftTail or root
        return last
    dfs(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(flatten(root))
