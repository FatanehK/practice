"""Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
class Solution:
    def encode(self,strs):
        result =""
        for s in strs:
            result += str(len(s))+"#"+s
        return result

    def decode(self,s):

        result =[]
        i =0
        while i< len(s):
            j = i
            while s[j]!= "#":
                j+=1
            lenght = int(s[i:j])
            result.append(s[j+1:j+1+lenght])
            i = j + 1 + lenght
        return result
strs = ["leet", "code"]
sol = Solution()
encoded = sol.encode(strs)
print("Encoded:", encoded)
decoded = sol.decode(encoded)
print("Decoded:", decoded)
