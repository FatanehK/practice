from collections import deque

class Graph:
    def __init__(self,adjc_dict={}) -> None:
        self.adjc_dict = adjc_dict



    def bfs(self,strat_node):
        graph = self.adjc_dict
        q = deque([strat_node])
        visited=[strat_node]
        if len(graph)== 0:
            return []

        while q:
            curr = q.popleft()
            for neighbor in self.adjc_dict[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.append(neighbor)
        return visited 
    

