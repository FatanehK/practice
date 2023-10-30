'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104'''


def maxArea(arr):

    max_area = 0
    r = len(arr)-1
    l = 0
    while l < r :
        area = (r-l)* min(arr[l],arr[r])
        max_area = max(area,max_area)
        if arr[l]< arr[r]:
            l+=1
        elif arr[l] >  arr[r]:
            r-=1
        else:
            r-=1
    return max_area
    # i = 0
    # j = len(arr)-1
    # max_area = 0
    # while i < j:
    #     area = (j-i) * min(arr[i], arr[j])
    #     max_area = max(area, max_area)
    #     i += 1
    # return max_area

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

