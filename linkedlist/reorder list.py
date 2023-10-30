class Node:
    def __init__ (self,val):
        self.val = val
        self.next= None

def reorder(head):
    # slow = head
    # fast= head
    # while fast and fast.next:
    #     slow= slow.next
    #     fast = fast.next.next
    if not head:
        return

        # find the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    # reverse the 2nd list
    prev= None
    curr= slow

    while curr:
        var = curr.next
        curr.next = prev
        prev= curr
        curr = var

    # merge the 2 lists
    first = head
    second = prev

    while second.next:
        temp = first.next
        first.next = second
        first = temp

        temp2 = second.next
        second.next = first
        second = temp2

    return head
#  Create the head node
head = Node(1)
curr= head

# Use a loop to add more nodes
for h in range(2,5):
    new_node = Node(h)
    curr.next = new_node
    curr = curr.next
# print(head.val)
print(reorder(head))