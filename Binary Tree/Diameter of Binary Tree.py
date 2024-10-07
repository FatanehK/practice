class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    diameter=0

    def height(node):
        nonlocal diameter
        if not node: return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(left +right, diameter)
        return 1+ max(left,right)
    height(root)
    return diameter


def run_tests():
    # Test case 1: Standard binary tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print("Test Case 1: Expected Diameter = 3, Actual Diameter =", diameterOfBinaryTree(root1))

    # Test case 2: Single node tree
    root2 = TreeNode(1)
    print(
        "Test Case 2: Expected Diameter = 0, Actual Diameter =",
        diameterOfBinaryTree(root2),
    )

    # Test case 3: Empty tree
    root3 = None
    print(
        "Test Case 3: Expected Diameter = 0, Actual Diameter =",
        diameterOfBinaryTree(root3),
    )


# Run the tests
run_tests()
