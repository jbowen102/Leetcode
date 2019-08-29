"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self, x):
        # Convert int to string and reverse the string.
        x_str = str(x)
        # If it's a negative number, move the negative sign.
        if x_str[0] == '-':
            x_str = x_str[1:] + x_str[0]
        rev_x_str = x_str[::-1]

        # Convert back to int.
        rev_x = int(rev_x_str)
        return rev_x













#
