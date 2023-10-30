'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

'''
def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    def inorder(r):
        if not r: return []
        return inorder(r.left) + [r.val] + inorder(r.right) 

    return inorder(root)[k - 1]
