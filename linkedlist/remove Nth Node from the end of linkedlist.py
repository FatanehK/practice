"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_nth_node(head, n):
    dummy = ListNode(0, head)
    right = head
    left = dummy

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


head = ListNode(1)
curr = head
for i in range(2, 6):
    new_node = ListNode(i)
    curr.next = new_node
    curr = curr.next

print(remove_nth_node(head, 2))
