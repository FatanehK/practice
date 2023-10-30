'''Write a method which accepts a sorted array of integers.
 The method should find the first pair where the sum is 0. Return an array that includes both 
 values that sum to 0 or nil if the pair does not exist.'''
# Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
# Output: 22 and 30

# Input: arr[] = {1, 3, 4, 7, 10}, x = 15
# Output: 4 and 10
def sum_zero(arr,x):
    map={}

    for i in range(len(arr)):
        num = arr[i]
        diff = x- num
        if diff not in map:
            map[num]=i
        else:
            return [i, map[diff]]
print(sum_zero([-1,0,1,2,37],0))
        