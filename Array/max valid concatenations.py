'''You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

["aa","bb"]
["a","b","c"]
'''
def maxLength(arr) -> int:

    exclude_idx=[]
    ans=""
    ordered_indexs = []
    for i, item in enumerate(arr):
        item_set = set(item)
        if len(item_set) != len(item):
            exclude_idx.append(i)
        else:
            ordered_indexs.append((i, len(item)))
    
    ordered_indexs.sort(key=lambda x: x[1], reverse=True)

    for c in range(len(arr)):
        included = set()
        done=True
        for i in range(len(arr)):
            if i not in exclude_idx:
                included_before = set(included)
                item = arr[i]                
                for char in item:
                    included.add(char)
                if len(included_before)+len(item) != len(included):
                    next = ordered_indexs.pop()
                    exclude_idx=next[0]
                    included = included_before
                    done=False
                    break
        if done:
            return len(included)
    return 0
        
    
print(maxLength(["cha", "r", "act", "ers"]))

                
                




        


    # map={}
    # new_list=[]

    # result = 0
    # Flag = True
    # for word in arr:
    #     for char in word:
    #         if char in map:
    #             Flag= False
    #             break
    #         else:
    #             map[char]=1
    #     if Flag:
    #         new_list.append(word)

    
    # for i in range(len(new_list)):
    #     for j in range(i+1,len(new_list)):    
    #         if new_list[j]!=new_list[i]:
    #             result = max(result, len(new_list[j])+len(new_list[i]))

    # return result if len(arr)!= 1 else len(arr[0])
