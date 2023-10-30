# def move_zero_one(arr):
#     count =0
#     for num in arr:
#         if num ==0:
#             count+=1
#     i =0
#     while i < len(arr):
#         if count > 0:
#             arr[i]=0
#             count-=1
#         else:
#             arr[i]= 1
#         i+=1

#     return arr
# print(move_zero_one([1,0,0,1,1]))

# def remove_zero(arr):
    # n= len(arr)
    # x = []
    # for i in range(n-1,-1,-1):
    #     if arr[i]==0:
    #         x.append(i)
    #     elif len(x):
    #         arr[x.popleft()]=arr[i]



# print(remove_zero([1,0,0,1,1]))

# def remove_duplicate(arr):
#     i =1
#     j=0
#     while i < len(arr):
#         if arr[i]!= arr[j]:
#             j+=1
#             arr[j]=arr[i]
#         i+=1
#     return arr


# print(remove_duplicate([0, 0, 1, 2,4,5]))
'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105'''


def non_repeating_character(s):
    hash_s={}
    for i, char in enumerate(s):
        count=0
        if not char in hash_s:
            hash_s[char]= [i,count+1]
        else:
            hash_s[char][1]+=1
            
    for value in hash_s.values():
        if value[1]== 1:
            return value[0]
        
    return -1
    # min_key = sorted(hash_s.values(), key= lambda x:x[1])
    # return min_key[0][0]
print(non_repeating_character("loveleetcode"))


def findTheDifference( s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    hash_s={}
    for char in s:
        hash_s[char]= hash_s.get(char,0)+1
    count=0
    result = ""
    for item in t:
        if item in hash_s:
            hash_s[item]-=1
        if hash_s.get(item) < 0:
            count+=1
            result +=item

    if count ==1:
        return result 


print(findTheDifference("a", "aa"))
