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

        nums.sort()

        # initialize best sum
        best_sum = nums[0]+nums[1]+nums[2]

        for i, num in enumerate(nums):
            target2 = target - num
            nums2 = nums.copy()
            nums2.remove(num)

            for j, num2 in enumerate(nums2):
                target3 = target2 - num2

                nums3 = nums2.copy()
                nums3.remove(num2)

                # perform binary search
                # pick mid-point (floor div).
                # if mid-point larger than target3, recurse on left half.
                # base case: only one item in search space.

# build algorithm that sorts input O(nlogn), then iterates through each item in
# outer loop then each item in inner loop (O(n^2)), then for final target val, use binary
# search (O(logn)). Overall alg O(nlogn + n^2 + logn) = O(n^2).
