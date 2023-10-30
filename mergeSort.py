def merge_sort(arry):
    if len(arry)>1:
        mid = len(arry)//2

        left= arry[:mid]
        right = arry[mid:]

        merge_sort(left)
        merge_sort(right)
        i =j= k=0

        while i <len(left) and j< len(right):
            if left[i]<= right[j]:
                arry[k] = left[i]

                i+=1
            else:
                arry[k]= right[j]
                j+=1

            k+=1
        while i <len(left):
            arry[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arry[k] = right[j]
            j+=1
            k+=1
    return arry
    
print(merge_sort([3,0,6,2]))