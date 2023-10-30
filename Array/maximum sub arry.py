def maxSubArray(nums) -> int:
    max_sum =nums[0]
    curr_sum= 0
    for num in nums:
        curr_sum = max(curr_sum,0)
        curr_sum+= num
        max_sum = max(curr_sum,max_sum)
    return max_sum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))