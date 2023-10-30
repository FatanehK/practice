class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def revese(head):
    curr = head
    prev= None
    while curr:
        nxt_node= curr.next
        curr.next = prev
        prev = curr
        curr = nxt_node
    return prev
        

list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('e', Node('d', Node('c', Node('b', Node('a')))))
assert revese(list_2) == expected
