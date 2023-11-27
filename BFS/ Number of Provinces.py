'''There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]'''
from collections import deque
def num_province(isConnected):


    n= len(isConnected)
    connect =0
    visited=[0]* n
    queue =deque([])
    while not all(visited):
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                break
        while queue:
            curr = queue.popleft()
            if not visited[curr]:
                for j in range(n):
                    if isConnected[curr][j]== 1 and curr!=j:
                        queue.append(j)
                visited[curr]= 1

        connect+=1
    return connect


print(num_province([[1,1,0],[1,1,0],[0,0,1]]))