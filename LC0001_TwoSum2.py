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

def twosum(nums, target):
    hash_map = dict()
    for i, x in enumerate(nums):
        hash_map[x] = [i, target-x]
    for num in hash_map.keys():
        # For every number, look for the number's complement in the dictionary keys
        complement = hash_map[num][1]
        if complement in hash_map.keys() and hash_map[num][0] != hash_map[complement][0]:
            return [hash_map[num][0], hash_map[complement][0]]
    return None

# modify this code so it correctly outputs [0, 1] for the [3, 3] input.
