class TreeNode:
    def __init__(self,val) -> None:
        self.val =val
        self.left =None
        self.right =None
class Tree:
    def __init__(self) -> None:
        self.root =None


def addBST(root,val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = addBST(root.left,val)
    else:
        root.right = addBST(root.right,val)
    return root
    

def searchBST(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

tree = Tree()
tree.root = TreeNode(19)
tree.root.left = TreeNode(7)
tree.root.right = TreeNode(25)
tree.root.left.left = TreeNode(5)
print(searchBST(tree.root,50))