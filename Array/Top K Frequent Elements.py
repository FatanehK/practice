"""Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."""

def top_frequent(arry,k):

    map ={}
    for num in arry:
        map[num] = map.get(num,0)+1
    sorted_map = max(sorted(map.items(), key= lambda x:x[0], reverse=True))
    print(sorted_map)
    # result = [n[0]for n in sorted_map[:k]]
    # return result


    # map = {}
    # for word in arry:
    #     map[word] = map.get(word, 0)+1
    # result = sorted(map.keys(), key=lambda word: (-map[word], word))

    # return result[:k]


print(top_frequent(["the", "day", "is", "sunny",
      "the", "the", "the", "sunny", "is", "is"], 4))

# class Codec:

#     def encode(self, strs):
#         """Encodes a list of strings to a single string.
        
#         :type strs: List[str]
#         :rtype: str
#         """
#         delimiter = '\#'
#         encoded_string = delimiter.join(strs)
#         return encoded_string

#     def decode(self, s):
#         """Decodes a single string to a list of strings.
        
#         :type s: str
#         :rtype: List[str]
#         """
#         delimiter = '\#'
#         decoded_strings = s.split(delimiter)
#         return decoded_strings
# x= Codec()
# p=x.encode(["hello","world"])
# print(x.decode(p))
