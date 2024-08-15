
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    # recurse from top down, but need to update boundraries!
    def valid(node, left, right):
        if not node: return True

        if node.val <= left or node.val >= right:
            return False
        left = valid(node.left, left, node.val)
        right = valid(node.right, node.val, right)
        return  left and right

    return valid(root, float("-inf"), float("inf"))
root= TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))
