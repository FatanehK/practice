'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109'''


def majorityElement(nums):
    if not nums:
        return []
    count1 =0
    count2 =0
    can1= None
    can2 =None
    for num in nums:
        if count1 == 0:
            can1 = num
            count1+=1
        elif count2 ==0:
            can2 = num
            count2 +=1
        elif can2 == num:
            count2+=1
        elif can1 == num:
            count1+=1
        else:
            count1 -=1
            count2 -=1
    count1 =0
    count2 =0
    for num in nums:
        if num == can1:
            count1+=1
        elif num == can2:
            count2 +=1
    n = len(nums)//3
    result =[]
    if count1 > n:
        result.append(can1)
    if count2 > n:
        result.append(can2)
    return result
print(majorityElement( [1,2,1,11,1,2,2]))