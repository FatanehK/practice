"""Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""


class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        count_zero = arr.count(0)
        for i in range(n - 1, -1, -1):
            if i + count_zero < n:
                arr[i + count_zero] = arr[i]
            if arr[i] == 0:
                count_zero -= 1
                if i + count_zero < n:
                    arr[i + count_zero] = 0

        # anothe approach
        i =0
        while i< len(arr):
            if arr[i]== 0:
                i+=1
                arr.insert(i,0)
                arr.pop()
            else:
                arr[i]= arr[i]
            i+=1
        


sol = Solution()
print(sol.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
