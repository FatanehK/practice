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

