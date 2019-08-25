"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twosum(nums, target):
    nums_len = len(nums)
    for i in range(len(nums)):
        if nums[i] <= target:
            for j in range(i+1, nums_len):
                if nums[i]+nums[j] == target:
                    return [i, j]
