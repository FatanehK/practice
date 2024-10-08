def Search_Rotated_Array(arry,target):
    low = 0
    high = len(arry)-1
    
    while low <= high:
        mid = (low+high)//2
        if arry[mid] == target:
            return mid
        elif arry[low] <= arry[mid]:
            if arry[low] <= target < arry[mid]:
                high= mid-1
            else:
                low= mid+1
        
        else:
            if arry[mid] < target <= arry[high]:
                low = mid+1
            else:
                high = mid-1
    return -1


print(Search_Rotated_Array([3,1],1))