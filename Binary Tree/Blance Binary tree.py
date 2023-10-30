def isBalanced(root):


    def valid(node):
        if not node: return [True,0]

        left = valid(node.left)
        right = valid(node.right)
        balance = left[0] and right[0] and abs(left[1]-right[1]<=1)# from root 
        return [balance, max(left[1],right[1]+1)]
    return valid(root)

