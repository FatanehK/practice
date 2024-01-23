"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    valid = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for char in s:
        if char in valid:
            stack.append(char)
        elif not stack or valid[stack.pop()] != char:
            return False
    if len(stack) > 0:
        return False
    return True


print(isValid("}"))


