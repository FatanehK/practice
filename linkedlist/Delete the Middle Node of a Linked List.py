class LinkedList:
    def __init__(self, value):
        self.val = value
        self.next = None


def deleteMiddle(head):
    curr = head
    curr_index = 0
    while curr:
        curr = curr.next
        curr_index += 1
    len = curr_index
    indx = curr_index//2
    
    curr= head
    curr_index=0
    while curr and curr_index < indx - 1:
        curr = curr.next
        curr_index += 1
    if curr and curr.next:
        curr.next = curr.next.next
    return head


head = LinkedList(0)
curr = head
for i in range(1, 6):
    curr.next = LinkedList(i)
    curr = curr.next
print(deleteMiddle(head))
