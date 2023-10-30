'''Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
Accepted
163.6K
Submissions
343.3K
Acceptance Rate
47.7%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Discussion (7)

'''
def isStrobogrammatic(num):
    """
    :type num: str
    :rtype: bool
    """
    map = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
    result = ""
    for n in num:
        if n not in map:
            return False
        else:
            result += map[n]
    return result[::-1] == num


print(isStrobogrammatic("89"))
