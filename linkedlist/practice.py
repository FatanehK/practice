class LinkNode:
    def __init__(self,val):
        self.val= val
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr_index =0
        curr = self.head
        while curr and curr_index < index:
            curr = curr.next
            curr_index+=1
        if curr:
            return curr.val
        
    def addAtHead(self, val):
        new_node = LinkNode(val)
        new_node.next= self.head
        self.head = new_node
        return self.head

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = LinkNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr =curr.next
            curr.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = LinkNode(val)
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        curr_index =0
        while curr and curr_index < index-1:
            curr =curr.next
            curr_index +=1
        if curr:
            new_node.next = curr.next
            curr.next = new_node


    
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None

        """
        if index == 0:
            self.head = self.head.next

        curr = self.head
        curr_index =0
        while curr and curr_index < index-1:
            curr =curr.next
            curr_index +=1
        if curr:
            curr.next = curr.next.next

ll = Linklist()
for i in range(1,5):
    ll.addAtTail(i)

curr = ll.head
while curr:
    print(curr.val, end= "->")
    curr= curr.next
print("None")

print(ll.addAtIndex(3, 5))
curr = ll.head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("None")
