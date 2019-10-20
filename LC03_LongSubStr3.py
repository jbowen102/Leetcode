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
        max_substring_score = 0

        start_index = 0
        stop_index = 0
        char_table = {}

        i = 0
        for char in s:
            print("\tbeginning of i=%d; " % i)
            if char in char_table:
                print("char \'%s\' in table:" % char)
                print(char_table)
                if stop_index-start_index > max_substring_score:
                    max_substring_score = stop_index - start_index
                    print(("%d" % start_index) + " -> " + ("%d" % stop_index) + "| " + s[start_index:stop_index])

                start_index = start_index + 1
                stop_index = start_index + 1
                char_table[char] = {}
                i = start_index + 1
                # have to restart the loop
                # maybe a recursive approach would be better
            else:
                print("char \'%s\' not in table" % char)
                print(char_table)
                char_table[char] = i
                stop_index = i+1

            print(char_table)
            print("\tend of i=%d; " % i)
            i += 1

        # account for when longest string is at end
        if stop_index-start_index > max_substring_score:
            max_substring_score = stop_index - start_index
            print(s[start_index:stop_index])

        return max_substring_score


# not finished



#
