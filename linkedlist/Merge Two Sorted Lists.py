class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists) :
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = Node(None)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


node_one = Node(1)
node_two = Node(2)
node_d = Node(3)
node_e = Node(5)
node_f = Node(9)
node_h= Node(10)
list1 =  node_one
node_one.next = node_two
node_two.next = node_d
node_d.next = node_e
node_e.next = node_f
node_f.next = node_h


node_a = Node(3)
node_b = Node(4)
node_c= Node(5)
node_four = Node(6)
node_a.next = node_b
node_b.next = node_c
node_c.next = node_four
list2 = node_a

node_a = Node(1)
node_b = Node(8)
node_c = Node(10)
node_four = Node(16)
node_a.next = node_b
node_b.next = node_c
node_c.next = node_four
list3 = node_a
sol= Solution()
print(sol.mergeKLists([list1,list2,list3]))