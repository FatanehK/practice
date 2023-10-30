from collections import deque



def validPath(n, edges, source, destination):

    graph = [[]for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = [source]
    while queue:
        curr = queue.popleft()
        if curr == destination:
            return True
        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return False
print( validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]],1, 5))