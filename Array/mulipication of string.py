
'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.'''

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    n1, n2 = len(num1), len(num2)
    result = [0] * (n1 + n2)
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            d2 = ord(num2[j]) - ord('0')
            temp = d1 * d2 + result[i + j + 1]
            result[i + j] += temp // 10
            result[i + j + 1] = temp % 10
    result_str = "".join(map(str, result))
    return result_str.lstrip('0') or '0'


print(multiply("123","456"))
# def countSeniors(details):
#     """
#     :type details: List[str]
#     :rtype: int
#     """
#     count = 0
#     for i in range(len(details)):
#         age = int(details[i][11:13])
#         if age > 60:
#             count += 1

#     return count
# print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))