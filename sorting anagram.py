'''Write a method to sort an array of strings so that all the anagrams are next to each other.'''

def soring_anagram(arry):

    def helper(string):
        return "".join(sorted(string))
    map={}
    for word in arry:
        a = helper(word)
        if a in map:
            map[a].append(word)
        else:
            map[a] =[word]
    print(map)
    result =[]
    for value in sorted(map.values()):
        result.append(value)
    # for key in sorted(map.keys()):
    #     result.extend(map[key])
    return result
print(soring_anagram( ["listen", "silent", "hello", "world", "act", "cat"]))


        