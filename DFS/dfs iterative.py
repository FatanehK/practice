class Graph:
    def __init__(self,adj_dict={}) -> None:
        self.adj_dict=adj_dict

def dfs(self,start_node):
    graph = self.adj_dict

    if len(graph)== 0:
        return []
    
    stack=[]
    visited =[]
    stack.append(start_node)
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited