"""Create a function possible_bipartition which takes in an adjacency list representing a graph of puppies, dislikes. 
The function should determine whether the puppies can be divided into two groups where no two puppies 
that dislike each other are in the same group."""
from collections import deque


# dislikes = {
#     "Fido": [],
#     "Nala": ["Cooper", "Spot"],
#     "Cooper": ["Nala", "Bruno"],
#     "Spot": ["Nala"],
#     "Bruno": ["Cooper"]
# }
dislikes = {
    "Fido": [],
    "Nala": ["Cooper", "Spot"],
    "Cooper": ["Nala", "Spot"],
    "Spot": ["Nala", "Cooper"]
}
# dislikes = {
#     "Fido": [],
#     "Rufus": [],
#     "James": [],
#     "Alfie": ["T-Bone"],
#     "T-Bone": ["Alfie", "Scruffy"],
#     "Scruffy": ["T-Bone"],
#     "Bruno": ["Nala"],
#     "Calico": ["Nala"],
#     "Nala": ["Bruno", "Calico"]
# }


def possible_bipartition(dislikes):



    unvisited= set(dislikes.keys())
    blue =set()
    red = set()
    queue = deque()
    while unvisited:
        s= unvisited.pop()
        red.add(s)
        queue.append(s)
        while queue:
            curr= queue.popleft()
            for n in dislikes[curr]:
                if n not in blue and n not in red:
                    if curr in red:
                        blue.add(n)

                    else:
                        red.add(n)

                else:
                    if ( n in blue and curr in blue ) or (n in red and curr in red):
                        return False
                    
        unvisited -=blue
        unvisited -=red
    return True













    # red = set()
    # blue =set()
    # unvisited = set(dislikes.keys())
    # while unvisited:
    #     S= unvisited.pop()
    #     red.add(S)
    #     queue = deque([S])
    #     while queue:
    #         curr = queue.popleft()
    #         for n in dislikes[curr]:
    #             if n not in red and n not in blue:
    #                 if curr in red:
    #                     blue.add(n)
    #                 else:
    #                     red.add(n)
    #                 queue.append(n)
    #             else:
    #                 if (curr in red and n in red) or (curr in blue and n in blue):
    #                     return False
    #     unvisited -=blue
    #     unvisited -=red
    # return True







    # blue = set()
    # red = set()
    # unvisited = set(dislikes.keys())
    # while unvisited:
    #     s = unvisited.pop()
    #     red.add(s)
    #     queue = deque([s])
    #     while queue:
    #         curr = queue.popleft()
    #         for n2 in dislikes[curr]:
    #             if n2 not in red and n2 not in blue:
    #                 if curr in red:
    #                     blue.add(n2)
    #                 else:
    #                     red.add(n2)
    #                 queue.append(n2)
    #             else:
    #                 if (curr in red and n2 in red) or (curr in blue and n2 in blue):
    #                     return False
    #     unvisited -= blue
    #     unvisited -= red
    # return True


print(possible_bipartition(dislikes))


# blue = set()
#  red = set()
#   unvisited = set(dislikes.keys())

#    while unvisited:
#         s = unvisited.pop()
#         red.add(s)
#         r = deque([s])
#         while r:
#             curr = r.popleft()
#             for n2 in dislikes[curr]:
#                 if n2 not in red and n2 not in blue:
#                     if curr in red:
#                         blue.add(n2)
#                     else:
#                         red.add(n2)
#                     r.append(n2)
#                 else:
#                     if (curr in blue and n2 in blue) or (curr in red and n2 in red):
#                         return False
#         unvisited -= red
#         unvisited -= blue
#     return True
