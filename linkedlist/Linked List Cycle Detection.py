"""Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:

Input: head = [1,2,3,4], index = 1

Output: true
"""
class Node:
    def __init__(self,val):
        self.next = None
        self.val =val
def has_cycle(head):
    fast = head 
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

ll = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

ll.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(ll))