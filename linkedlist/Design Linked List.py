class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        curr_indx = 0
        curr = self.head
        while curr and curr_indx <= index:
            if curr_indx == index:
                return curr.val
            else:
                curr = curr.next
                curr_indx += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val, self.head)
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = ListNode(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            new_node = ListNode(val, self.head)
            self.head = new_node
            return
        curr = self.head
        curr_indx = 0
        while curr and curr_indx < index-1:
            curr = curr.next
            curr_indx += 1
        if curr:
            new_node = ListNode(val, curr.next)
            curr.next = new_node

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        curr_indx = 0
        curr = self.head
        while curr and curr_indx < index-1:
            curr = curr.next
            curr_indx += 1

        if curr and curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
