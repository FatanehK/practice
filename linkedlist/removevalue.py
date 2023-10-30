class Node:
    def __init__(self,value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

def removeElements(head, val):
    """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
    """
    if not head:
        return head
    if head and head.val == val:
        head = head.next

    
    curr = head
    while curr:
        if curr.next and curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

      # Check if the value was not found in the entire list
    if not head:
        return -1  # Return -1 if the value was not found
    else:
        return head  # Return the modified list


node_one = Node(1)
node_two = Node(2)

list1 = node_one
node_one.next = node_two

print(removeElements(list1, 1))

head = LinkedList(1)
for i in range(2,6):
    head.next = LinkedList(i)
    head = head.next
