class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    
    if not root:
        return 0
    diameter = 0
    # Initialize diameter as 0


    def height(node):
        nonlocal diameter
        if not node:
            return 0
        # recursively find the longest path in
        # both left child and right child
        left = height(node.left)
        right = height(node.right)
        # Update the diameter if necessary
        diameter = max(diameter, left + right)
        # Return the height of the current node
        return 1 + max(left, right)


    # Start the height calculation from the root
    height(root)
    
    return diameter


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_depth(root))
