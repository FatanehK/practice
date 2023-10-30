class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def get (head,index):

    curr_index = 0
    curr = head

    while curr and curr_index< index:
        curr_index+=1
        curr =curr.next
    if curr and curr_index == index:
        return curr. val

def add_at_head(head,val):
    new_node = Node(val)
    new_node.next = head
    head = new_node
    return head


head = Node(1)
curr = head
for i in range(2,6):
    curr.next = Node(i)
    curr = curr.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# head = add_at_head(head,10)
# print_linked_list(head)


def add_at_tail(head, val):
    new_node = Node(val)

    if not head:
        head = new_node

    else:
        curr= head
        while curr.next:
            curr = curr.next
        curr.next = new_node



def add_at_index(head, index,val):
    new_node = Node(val)
    if index == 0:
        add_at_head(val)
        return 
    
    curr_index =0
    curr = head
    while curr and curr_index< index -1:
        curr = curr.next
        curr_index +=1

    if curr:
        new_node.next = curr.next
        curr.next = new_node


add_at_tail(head,10)
print_linked_list(head)