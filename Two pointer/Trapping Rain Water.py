'''Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.


Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9'''


def traping_rain_water(height):
    result =0
    left_max= []
    for h in height:
        if not left_max:
            left_max.append(h)
        else:
            left_max.append(max(left_max[-1],h))
    right_max= 0

    for i in range(len(height)-1,-1,-1):
        if i >0:
            leftof_me = left_max[i-1]
        else:
            leftof_me =0

        rlmin = min(leftof_me,right_max)
        if rlmin > height[i]:
            result += rlmin - height[i]
        right_max = max(right_max,height[i] )

    return result


print(traping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
