'''Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]'''

import heapq
def topKFrequent( words, k):
    count ={}
    for word in words:
        count[word]= count.get(word,0)+1
    print(count)

    pq = []
    # O(m log k), where m is the number of unique words and k is the number of most frequent words to be returned.
    for key, value in count.items():
        heapq.heappush(pq, (-value, key))

    result =[]
    # The heap pop operation has a time complexity of O(log m) where m is the size of the heap. In the worst case, this loop will run k times, resulting in O(k log m) time complexity.
    for _ in range(k):
        result.append(heapq.heappop(pq)[1])
    return result
    #  O(m + k log m)
print(topKFrequent( ["the","day","is","sunny","the","the","the","sunny","is","is"], 4))