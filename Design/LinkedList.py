'''Design Singly Linked List
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guranteed to be greater than or equal to 0.'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            raise IndexError("index must be posi")
        curr = self.head
        curr_index = 0
        while curr and curr_index <= index:   # curr_index <= index
            if curr_index == index:
                return curr.val
            curr = curr.next
            curr_index += 1
        return -1

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            new_node = ListNode(val)
            curr = self.head
            while curr.next:     # remeber to check curr.next is not None
                curr = curr.next
            curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next    # remeber 
    
        curr_indx = 0
        curr = self.head
        while curr and curr_indx < index-1:
            curr = curr.next
            curr_indx += 1

        if curr and curr.next:
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self):
        self.values = []
        curr = self.head
        while curr:
            self.values.append(curr.val)
            curr = curr.next
        return self.values

    def removeElement(self,head,val):
        dummy = ListNode()
        prev= dummy
        curr= head
        while curr:
            nxt_node = curr.next
            if curr.val == val:
                prev.next = nxt_node
            else:
                prev =curr
            curr = nxt_node
        return dummy.next
