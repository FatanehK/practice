'''Write an efficient function that checks whether any permutation of an input 
string is a palindrome. 
'''
def is_permutation_pal(string):
    map={}
    for char in string:
        map[char]= map.get(char,0)+1
    count_odd =0
    for value in map.values():
        if value % 2!=0:
            count_odd +=1
    return count_odd<=1

print(is_permutation_pal("ivxvci"))
'''Given two strings, write a method to determine if they are anagrams.'''
def anagram(string1,string2):
    if len(string1)!= len(string2):
        return False
    map_str1 ={}

    for char in string1:
        map_str1[char]= map_str1.get(char,0)+1

    for char2 in string2:
        if map_str1.get(char2,0) >0:
            map_str1[char2] -=1
        else:
            return False
    return True


print(anagram("listen","slent"))
