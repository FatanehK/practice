class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def min_node(self, node):
        while node.left:
            node = node.left
        return node

    def helper(self, node, key):
        if not node:
            return
        if node.val < key:
            node.right = self.helper(node.right, key)
        elif node.val > key:
            node.left = self.helper(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_right = self.min_node(node.right)
                node.val = min_right.val
                node.right = self.helper(node.right, node.val)
        return node

    def deleteNode(self, root, key):
        if not root:
            return
        return self.helper(root, key)

bst = Node(5)
bst.left = Node(3)
bst.left.left = Node(2)
bst.left.right = Node(4)
bst.right = Node(8)
bst.right.left = Node(7)
bst.right.right = Node(9)
ll = Solution()
print(ll.deleteNode(bst,5))