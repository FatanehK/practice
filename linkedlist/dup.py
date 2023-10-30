# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value
        # if next is None, this is the last element in the list
        self.next = next


def remove_duplicates(head):

    curr = head
    while curr and curr.next :
        if curr .value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


def are_linked_lists_equal(list1, list2):
    if list1 is None and list2 is None:
        return True
    if list1 is None or list2 is None:
        return False
    if list1.value == list2.value:
        return are_linked_lists_equal(list1.next, list2.next)
    # if list1 is None and list2 is None:
    #     return True
    # if list1 is None or list2 is None:
    #     return False
    # if list1.value != list2.value:
    #     return False
    # return are_linked_lists_equal(list1.next, list2.next)


list_1 = Node(7, Node(7, Node(7, Node(7))))
expected_1 = Node(7)
assert are_linked_lists_equal(remove_duplicates(list_1), expected_1)
