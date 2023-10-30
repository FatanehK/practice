class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None





def is_vaild_bst(curr, min_val, max_val):
    if not curr:
        return True
    if curr.key <= min_val or curr.key >= max_val:
        return False

    return (is_vaild_bst(curr.left, min_val, curr.key) and (is_vaild_bst(curr.right, curr.key, max_val)))


def is_BST(root):
    return is_vaild_bst(root, min, max)


root = Tree(2)
root.right = Tree(3)
root.left = Tree(1)

print(is_BST(root))




class Solution(object):
    def is_valid_bst(self,curr,min_val,max_val):
        if not curr:
            return True
        if curr.val <= min_val or curr.val >= max_val:
            return False

        return self.is_valid_bst(curr.left,min_val,curr.val)and self.is_valid_bst(curr.right,curr.val,max_val)
 


    def isValidBST(self,root):
        min_n = float("-inf")
        max_n = float("inf")
        return self.is_valid_bst(root,min_n,max_n)