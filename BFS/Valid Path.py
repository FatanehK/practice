"""
There is a bi-directional (undirected) graph with n vertices, where each vertex is labeled from 0 to n - 1.

The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [uᵢ, vᵢ] denotes an edge between vertex uᵢ and vertex vᵢ. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers, n, source, and destination, return True if there is a valid path from source to destination, or False otherwise.

Example:

       0 ------ 1
        \      /
         \    /
          \  /
            2

Input: n = 3, edges = [[[0,1],[1,2],[2,0]]], source = 0, destination = 2
Output: True

There are two paths that exist between node 0 and node 2:
- 0 -> 2
- 0 -> 1 -> 2

Please note there is no need to store the path to the node. You are only required to return whether the path exists (True or False).
"""
from collections import defaultdict, deque


def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q = deque([source])
    visited = set()
    visited.add(source)
    while q:
        curr = q.popleft()
        if curr == destination:
            return True
        for nei in graph[curr]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
    return False


print(validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
n = 3
edges = [[0, 1], [2, 1], [2, 0]]
source = 0
dest = 2

assert validPath(n, edges, source, dest) == True
"""
   1            3
  /             | \
 /              |  \
0               |   5
 \              |  /
  \             | /
   2            4
"""
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
dest = 5

assert validPath(n, edges, source, dest) == False
"""
   1 
  /
 /
0
 \ 
  \ 
   2
"""
n = 3
edges = [[0, 1], [2, 0]]
source = 2
dest = 1

assert validPath(n, edges, source, dest) == True

print("All tests passed! If time remains discuss time and space complexity")
