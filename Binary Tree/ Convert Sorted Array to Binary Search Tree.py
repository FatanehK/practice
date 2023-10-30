'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.
Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

'''
class TreeNode:
    def __init__(self,key):
        self.key =key
        self.right=None
        self.left =None
def heightbalanced_bineryTree(nums):

    def helper(l,r):
        if l > r:
            return None
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = helper(l,mid-1)
        root.right = helper(mid+1,r)
        return root
    return helper(0, len(nums)-1)

