'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
'''


def findOrder(numCourses, prerequisites):

    pre_hash = {i:[]for i in range(numCourses)}
    for crs ,pre in prerequisites:
        pre_hash[crs].append(pre)

    visit= set()
    cycle= set()
    answer=[]

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        cycle.add(crs)
        for pre in pre_hash[crs]:
            if not dfs(pre):
                return False

        visit.add(crs)
        cycle.remove(crs)
        answer.append(crs)
        return True
    for c in range(numCourses):
        if dfs(c) == False:
            return answer
    return answer


print(findOrder(4, [[0,1],[1, 0], [2, 0], [3, 1], [3, 2]]))

