class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    
    def valid(root,subRoot):
        if not root and not subRoot :return True
        if root and subRoot and root.val == subRoot.val:
            return valid(root.left,subRoot.left) and valid(root.right,subRoot.right)
    if not subRoot: return True
    if not root:return False
    if valid(root,subRoot):return True

    return isSubtree(root.left,subRoot) or isSubtree(root.right,subRoot)

root = TreeNode(3)
root.left =TreeNode(4)
root.left.left= TreeNode(1)
root.left.right = TreeNode(2)
root.right= TreeNode(5)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
print(isSubtree(root,subRoot))
