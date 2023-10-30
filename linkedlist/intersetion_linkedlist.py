def isthere_intersection(head_a,head_b):
    # l1 = head_a
    # while l1:
    #     l2= head_b
    #     while l2:
    #         if l1.val == l2.val:
    #             return l1
    #         l2 = l2.next
    #     l1= l1.next

    # return None


    curA= head_a
    curB =head_b
    a,b =0,0

    while curA:
        a+=1
        curA = curA.next

    while curB:
        b+=1
        curB = curB.next

    if a> b:
        curL=  curA
        diff = a-b
        curS = curB
    else:
        curL = curB
        diff = b-a
        curS = curA
    i =0
    while i < diff:
        curL=curL.next
        i+=1

    while curL!= curS:
        curL =curL.next
        curS =curS.next
    return curL





