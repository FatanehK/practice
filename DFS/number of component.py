'''You have a graph of n nodes. 
You are given an integer n and an array edges where edges[i] = [ai, bi] 
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.'''

from collections import deque
from collections import defaultdict

def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    graph = defaultdict(list)
    for src, des in edges:
        graph[src].append(des)
        graph[des].append(src)
    count=0
    visited= [0]* n
    queue = deque()
    while not all(visited):
        for i in range(n):
            if visited[i] ==0:
                queue.append(i)
                break
                
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if visited[neighbor] == 0 and  neighbor not in queue:
                    queue.append(neighbor)
            visited[curr] = 1
        count+=1
    return count






#     graph = defaultdict(list)
#     for a, b in edges:
#         graph[a].append(b)
#         graph[b].append(a)
#     visited = n * [0]
#     queue = deque()
#     connected = 0
#     while not all(visited):
#         for i in range(n):
#             if visited[i] == 0:
#                 queue.append(i)
#                 break
#         while queue:
#             curr = queue.popleft()
#             for neighbor in graph[curr]:
#                 if visited[neighbor] == 0 and neighbor not in queue:
#                     queue.append(neighbor)
#             visited[curr] = 1
#         connected += 1
#     return connected
print(countComponents(4,[[2,3],[1,2],[1,3]]))