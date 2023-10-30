"""Find the longest substring of a string containing `k` distinct characters
Given a string and a positive number k, find the longest substring of the string containing k distinct characters. 
If k is more than the total number of distinct characters in the string, return the whole string."""

CHAR_RANGE = 128

def findlongestsubstring(str,k):

    low =high =0
    begin = end = 0
    window = set()
    freq = [0]*CHAR_RANGE

    while high < len(str):

        window.add(str[high])
        freq[ord(str[high])] = freq[ord(str[high])]+1

        while len(window)> k:
            freq[ord(str[low])] = freq[ord(str[low])]-1
            if freq[ord(str[low])] == 0:
                window.remove(str[low])

            low +=1
        
        if end - begin < high-low:
            end = high
            begin = low

        high += 1

    return str[begin:end+1]
    




print(findlongestsubstring("strrt", 2))

    




# Function to find the longest substring of a given containing
# `k` distinct characters using a sliding window
# def findLongestSubstring(s, k):

#     # stores the longest substring boundaries
#     end = begin = 0

#     # set to store distinct characters in a window
#     window = set()

#     # `freq` stores the frequency of characters present in the
#     # current window. We can also use a dictionary instead.

#     freq = [0] * CHAR_RANGE

#     # `[low…high]` maintains the sliding window boundaries
#     low = high = 0

#     while high < len(s):

#         window.add(s[high])
#         freq[ord(s[high])] = freq[ord(s[high])] + 1

#         # if the window size is more than `k`, remove characters from the left
#         while len(window) > k:

#             # If the leftmost character's frequency becomes 0 after
#             # removing it in the window, remove it from the set as well
#             freq[ord(s[low])] = freq[ord(s[low])] - 1
#             if freq[ord(s[low])] == 0:
#                 window.remove(s[low])

#             low = low + 1        # reduce window size

#         # update the maximum window size if necessary
#         if end - begin < high - low:
#             end = high
#             begin = low

#         high = high + 1

#     # return the longest substring found at `s[begin…end]`
#     return s[begin:end + 1]


# print(findLongestSubstring("abcbdbxdbbcc", 3))
