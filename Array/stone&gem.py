"""Given two strings g (gems) and s (stones), find how many stones are gems.
 Ex. g = "aA", s = "aAAABb", output = 4 
At completion: optimize solution, identify time complexity(ies) of solution(s)"""


def gems_stones(g,s):

    count =0
    for char in s:
        if char in g:
            count +=1
    return count
print(gems_stones("aA", "aAAABb"))