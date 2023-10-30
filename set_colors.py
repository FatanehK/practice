"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function"""


def set_color(nums):
    left =0
    mid =0
    right = len(nums)-1
    while mid <= right:
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left],nums[mid]
            mid+=1
            left+=1
        elif  nums[mid] == 1:
            mid+=1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -=1
    return nums



print(set_color([2,0,2,1,1,0]))
