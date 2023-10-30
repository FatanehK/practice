class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next= next


def remove_nth_node(head,n):

    dummy = ListNode(0,head)
    right = head
    left = dummy

    while n > 0:
        right = right.next
        n-=1

    while right:
        left= left.next
        right= right.next

    left.next = left.next.next
    return dummy.next

head = ListNode(1)
curr= head
for i in range(2,6):
    new_node = ListNode(i)
    curr.next = new_node
    curr = curr.next

print(remove_nth_node(head, 2))
