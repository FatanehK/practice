def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j =1
    for i in range(1,len(nums)):
        if nums[i]!= nums[i-1]:
            nums[j]= nums[i]
            j+=1
    return nums[:j]




    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i]
        else:
            i += 1
    return nums

print(removeDuplicates([-1,0,0,2,2]))
