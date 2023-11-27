"""There are N students in a class. Some of them are friends, while some are not.
 Their friendship is transitive in nature. 
 For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
 If M[i][j] = 1, then the i-th and j-th students are direct friends with each other,
   otherwise not. And you have to output the total number of friend circles among all 
   the students.
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2"""
from collections import deque


def friendCircles(M):
    n = len(M)
    visited = [0] * n
    q = deque([])
    connect = 0
    while not all(visited):
        for i in range(len(visited)):
            if not visited[i]:
                q.append(i)
                break
        while q:
            curr = q.popleft()
            if not visited[curr]:
                for j in range(n):
                    if M[curr][j] == 1 and curr != j:
                        q.append(j)
                visited[curr] = 1
        connect += 1
    return connect


print(friendCircles([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
