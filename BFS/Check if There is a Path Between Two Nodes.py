"""Given a graph, represented as an adjacency list, and two nodes, source and destination, 
determine if there is a path from source to destination."""


from collections import deque
def path_exist(graph, source, destination):
    seen= set()
    queue = deque([source])
    while queue:
        curr = queue.popleft()
        if curr== destination:
            return True
        if curr not in seen:
            seen.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in seen:
                    queue.append(neighbor)
    return False
# graph = {0: [1, 2], 1: [2, 3], 2: [4], 3: [], 4: []}
# source = 0
# destination = 3
graph = {0: [1, 2], 1: [2], 2: [], 3: [4], 4: []}
source = 0
destination = 4
print(path_exist(graph, source, destination))
