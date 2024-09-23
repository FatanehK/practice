# next greater element

def next_greater_element(nums):
    stack =[]
    n = len(nums)
    result = [-1]* n

    for i in range(n):
        while stack and nums[i]> nums[stack[-1]]:
            idx = stack.pop()
            result[idx]= nums[i]
        stack.append(i)
    return result 

print(next_greater_element([2,1,3,2,4,3]))



