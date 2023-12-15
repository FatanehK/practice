"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
"""


def countBits(n):
    # dp = [0] * (n + 1)
    # for i in range(1, n + 1):
    #     dp[i] = dp[i >> 1] + (i & 1)
    # return dp
    
    # differnt approach 
    def count(n):
        result =0
        while n:
            result += n & 1
            n = n >> 1
        return result 

    arry =[] 
    for i in range(n+1):
        arry.append(count(i))
    return arry


print(countBits(5))
