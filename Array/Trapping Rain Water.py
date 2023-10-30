'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105'''

def trapping_water(height):
    left_max=[]
    res =0
    for i,h in enumerate(height):
        if not left_max:
            left_max.append(h)
        else:
            left_max.append(max(left_max[-1],h))
    rmax=0
    for i in range(len(height)-1,-1,-1):

        if i > 0:
            leftofme = left_max[i-1]
        else:
            leftofme =0

        lrmin = min(rmax, leftofme)
        if lrmin> height[i]:
            res += lrmin - height[i]
        rmax = max(rmax,height[i])
    return res
print(trapping_water([0,1,0,2,1]))