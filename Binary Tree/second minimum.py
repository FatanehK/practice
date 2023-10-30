class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def findSecondMinimumValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    values=[]
    def inorder(root):
        if not root: return []
        else:
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
    inorder(root)
    min_v = min(values)
    print(values)
    second = float('inf')
    for n in values:
        if n < second and n!= min_v:
            second = n
    return second if second != float('inf') else -1

bst = Node(2)
bst.left = Node(2)
bst.right = Node(5)
bst.right.left = Node(5)
bst.right.right = Node(7)

print(findSecondMinimumValue(bst))


def findSecondSmallestWithDuplicates(nums, smallest):
    second_smallest = float('inf')
    for num in nums:
        if num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else -1


# Example usage:
sorted = [2, 2, 4, 4, 5, 6, 6,7]
print(findSecondSmallestWithDuplicates(sorted,2))
