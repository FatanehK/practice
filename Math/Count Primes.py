"""Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106"""
def countPrimes(n):
    if n <= 2:
        return 0
    dp= [True for i in range(n)]
    dp[0]=False
    dp[1]=False
    for num in range(2,n):
        if dp[num]:
            for i in range(2*num,n,num):
                dp[i]= False
    return sum(dp)
print(countPrimes(6))