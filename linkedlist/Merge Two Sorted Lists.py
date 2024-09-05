"""ou are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Merge_two_sorted_list(list1, list2):
    if not list1 and not list2:
        return None
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # If one of the lists is not empty, append the remaining part to the merged list
    if list1:
        curr.next = list1
    else:
        curr.next = list2
    return dummy.next


ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(5)


ll2 = ListNode(3)
ll2.next = ListNode(4)


def print_linked_list(head: ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


# Merge the lists
merged_head = Merge_two_sorted_list(ll1, ll2)

# Print the merged list
print_linked_list(merged_head)
