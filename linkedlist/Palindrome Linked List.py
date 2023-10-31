class ListNode:
    def __init__(self,val,next =None):
        self.val = val
        self.next = next

def reverse(head):
    curr = head
    ans= None
    while curr:
        nxt = curr.next
        curr.next = ans
        ans= curr
        curr= nxt
    return ans


def Palindrome_Linked_List(head):
    N= 0
    curr = head
    while curr:
        N+=1
        curr = curr.next
    mid = N//2
    i =0
    first= second =head
    while i< mid:
        second = second.next
        i+=1
    second= reverse(second)
    while first and second:
        if first.val!= second.val:
            return False
        first = first.next
        second = second.next
    return True



def Palindrome_Linked_List(head):
    making a data structure
    nums=[]
    while head:
        nums.append(head.val)
        head = head.next
    l=0
    r = len(nums)-1
    while l<= r:
        if l.val != r.val:
            return False
        l= l.next
        r= r.next
    return True


def Palindrome_Linked_List(head):
    # find the middle 
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse the second half
    prev= None
    curr= slow
    while curr:
        nxt_node = curr.next
        curr.next= prev
        prev = curr
        curr = nxt_node

    # compare 
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first= first.next
        second = second.next
    return True


ll= ListNode("1")
ll.next = ListNode("2")
ll.next.next = ListNode("5")
ll.next.next.next = ListNode("1")
print(Palindrome_Linked_List(ll))
