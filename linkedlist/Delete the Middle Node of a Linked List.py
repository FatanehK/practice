"""You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""


class LinkedList:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def deleteMiddle(head):
    # curr = head
    # curr_index = 0
    # while curr:
    #     curr = curr.next
    #     curr_index += 1
    # len = curr_index
    # indx = curr_index // 2

    # curr = head
    # curr_index = 0
    # while curr and curr_index < indx - 1:
    #     curr = curr.next
    #     curr_index += 1
    # if curr and curr.next:
    #     curr.next = curr.next.next
    # return head
    # another approach
    Dummy = LinkedList(0, head)
    left = Dummy
    right = head
    while right and right.next:
        left = left.next
        right = right.next.next
    left.next = left.next.next
    return Dummy.next


head = LinkedList(1)
curr = head
for i in range(2, 6):
    curr.next = LinkedList(i)
    curr = curr.next
print(deleteMiddle(head))
