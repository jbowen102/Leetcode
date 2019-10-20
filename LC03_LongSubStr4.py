"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int
    def lengthOfLongestSubstring(self, s):
        buffer = ''
        max_buffer = ''
        loc_table = {}          # To store indices of characters in buffer.

        for i, new_char in enumerate(s):

            if new_char in buffer:
                pos = loc_table.get(new_char)

                # Update buffer
                buffer = s[pos+1:i+1]

            else:
                buffer += new_char

            loc_table[new_char] = i

            if len(buffer) > len(max_buffer):
                max_buffer = buffer

        return len(max_buffer)


# 64ms runtime on Leetcode
# 14MB mem usage
