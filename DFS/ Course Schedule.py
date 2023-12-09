"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses"""

from collections import defaultdict, deque

# def canFinish(numCourses, prerequisites):
#     """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#     """
#     visited = set()
#     cors_hash = {i: [] for i in range(numCourses)}
#     for cors, pre in prerequisites:
#             cors_hash[cors].append(pre)

#     def dfs(cors):
#         if cors_hash[cors] == []:
#             return True
#         if cors in visited:
#             return False
#         visited.add(cors)
#         for pre in cors_hash[cors]:
#             if dfs(pre) == False:
#                 return False
#         visited.remove(cors)
#         cors_hash[cors] = []
#         return True

#     for c in range(numCourses):
#         if dfs(c) == False:
#             return False
#     return True

from collections import defaultdict


class Solution:
    def canFinish(numCourses, prerequisites) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        circle = set()
        visited = set()

        def dfs(crs):
            if crs in circle:
                return False
            if crs in visited:
                return True
            circle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            circle.remove(crs)
            visited.add(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


def canFinish(numCourses, prerequisites):
    # Build a directed graph and count in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with nodes having in-degree 0
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # Perform topological sorting
    while queue:
        course = queue.popleft()
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses are processed, return True; otherwise, return False
    return sum(in_degree) == 0


# Example usage:
numCourses1 = 2
prerequisites1 = [[1, 0]]
print(canFinish(numCourses1, prerequisites1))  # Output: True

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(canFinish(numCourses2, prerequisites2))  # Output: False

# return True


# print(canFinish(2,[[1,0]]))
