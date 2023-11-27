"""Search in Rotated Array: Given a sorted array of n integers that has been 
rotated an unknown number of times, write code to find an element in the array. 
You may assume that the array was originally sorted in increasing order."""


def search_rotated_sorted_arry(arry, target):
    left = 0
    right = len(arry)-1
    while left <= right:
        mid = (right+ left)//2
        if arry[mid] == target:
            return mid
        if arry[left] < arry[mid]:
            if arry[left] <= target< arry[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if arry[mid]< target <= arry[right]:
                left = mid+1
            else:
                right = mid-1
    return -1
print(search_rotated_sorted_arry([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],5))


def merge_sorted_arry(nums1, m, nums2, n):
    i = m - 1  # Index for nums1
    j = n - 1  # Index for nums2
    k = m + n - 1  # Index for the merged array

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1
print(merge_sorted_arry([1, 2, 3, 0, 0, 0],3, [2, 5, 6], 3))


def test():
    result = merge_sorted_arry([1, 2, 3, 0, 0, 0],3, [2, 5, 6], 3)
    assert result == [1,2,2,3,5,6]
test()
print("all test is passed!")
