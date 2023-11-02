'''Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.



Problem Constraints
1 <= N <= 105

1 <= A[i][0] <= A[i][1] <= 109



Input Format
First and only argument is a 2D array A of size N x 2 denoting the N intervals.



Output Format
Return a integer denoting the length of maximal set of mutually disjoint intervals.



Example Input
Input 1:

 
Input 2:'''
A = [
  [4, 4],
  [8, 15],
  [6, 6],
  [2, 13],
  [2, 12]
]

def solve(A):
    A.sort(key= lambda x:x[1])
    print(A)
    result =A[0][1]
    count=1
    for r in range(len(A)):
        if A[r][0] > result:
            count+=1
            result = A[r][1]
    return count
        
print(solve(A))