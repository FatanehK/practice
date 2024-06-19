'''Input: n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
Output: True

Explanation:
    0
   /|\
  1 2 3
   |
   4
This graph is a valid tree.'''

def valid_tree(n,edges):
    adjaceny_list = {i:[]for i in range(n)}
    visited = set()
    for u,v in edges:
        adjaceny_list[u].append(v)
        adjaceny_list[v].append(u)
    def dfs(node,parent):
        visited.add(node)
        for neighbor in adjaceny_list[node]:
            if neighbor== parent:
                continue
            if neighbor in visited:
                return False
            if not dfs(neighbor,node):
                return False
        return True
    return dfs(0,-1) and len(visited) == n
print(valid_tree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))
