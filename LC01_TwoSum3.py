"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Idea to store complement of each number as value in dict:
https://leetcode.com/problems/two-sum/discuss/360014/Python3%3A-2-line-solution-faster-than-99-48ms

https://leetcode.com/problems/two-sum/discuss/360049/Python-3-solution-can-someone-tell-me-why-this-solution-is-too-slow-like-5664-ms
"""

# First, look in hash table for the num.
# If not there, calc complement and store that w/ the num's index.
# This way, when the complement is encountered in the input list, it will already
# have an entry in the hash table to use for retrieving the index of the matching
# num.

def twosum(nums, target):
    hash_map = dict()
    for i, num in enumerate(nums):
        complement = target - num
        if num in hash_map:
            return [hash_map[num], i]
        elif num <= target:
            hash_map[complement] = i
        else:
            continue

# 56ms runtime on Leetcode


# critical test cases: (nums = [3, 3], target = 6), (nums = [3, 2, 4], target = 6)
