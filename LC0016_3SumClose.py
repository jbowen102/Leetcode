"""
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest(self, nums, target):
        for i, num in enumerate(nums):
            target2 = target - num

            nums2 = nums.copy()
            nums2.remove(num)
            other_two = twosum(nums2, target2)
            if other_two:
                j = other_two[0]
                k = other_two[1]
                return [i, j, k]
                # need to return the sum instead.

    # Taken from TwoSum3 then revised:
    def twosum(nums, target):
        hash_map = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if num in hash_map:
                return [hash_map[num], i]
                # need to return the sum instead
            elif num <= target:
                hash_map[complement] = i
            else:
                continue
