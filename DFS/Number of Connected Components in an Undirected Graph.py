'''"Number of Connected Components in an Undirected Graph" can be stated as follows:

You are given an undirected graph with n nodes, where each node is uniquely labeled from 0 to n - 1. You are also given an array edges, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

A connected component is a set of nodes such that there is a path between every pair of nodes. The number of connected components in the graph is the number of distinct sets of nodes in the graph.

Write a function to return the number of connected components in the undirected graph.

Example:

Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Explanation: The graph has 2 connected components: [0, 1, 2] and [3, 4].

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.'''

from collections import deque
from collections import defaultdict
def number_of_connected(n, edges):
    visited= [0]* n
    connect=0
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    queue= deque([])
    while not all(visited):
        for i in range(len(visited)):
            if not visited[i]:
                queue.append(i)
                break
        while queue:
            curr= queue.popleft()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)
            visited[curr]=1
        
        connect +=1
    return connect 
        

print(number_of_connected(5,[[0, 1], [1, 2], [3, 4]]))
