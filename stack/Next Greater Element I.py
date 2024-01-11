def nextGreaterElement(nums1, nums2):
    next_greater = {}
    stack = []

    # Iterate through nums2 to find the next greater element using a stack
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Retrieve the next greater element for each element in nums1 from the dictionary
    result = [next_greater.get(num,-1) for num in nums1]

    return result


print(nextGreaterElement([4, 1, 2],[1, 3, 4, 2]))
