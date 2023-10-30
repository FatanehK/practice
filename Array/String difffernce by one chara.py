def differByOne(dict):
    """
    :type dict: List[str]
    :rtype: bool
    """
   
#     def one_differnce(word1,word2):
#         hash_map = {}
#         for i,char in enumerate(word1):
#             if i not in hash_map:
#                 hash_map[i]=[char,1]
#             else:
#                 hash_map[i][1] +=1
#         count = 0
#         for j,char in enumerate(word2):

#             if hash_map[j][0] ==  char :
#                 continue
#             else:
#                 count+=1
#         if count == 1 :
#             return True
#         else: return False
        
#     result =set()
#     for i in range(len(dict)):
#         for j in range(i+1,len(dict)):
#             if one_differnce(dict[i], dict[j]) and dict[i]!= dict[j]:
#                 result.add((dict[i],dict[j]))
    
#     return len(result)>=1 
# # print(one_differnce("abcd","aacd"))
print(differByOne(["abcd","acbd", "aacd"]))
            