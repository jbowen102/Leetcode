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

                num3 = self.bin_search(target3, nums3)

                new_sum = num + num2 + num3

                if abs(new_sum - target) < abs(best_sum - target):
                    best_sum = new_sum

        return best_sum


    def bin_search(self, target, array):
        # print(array)
        # base case
        if len(array) == 1:
            return array[0]
        elif len(array) == 2:
            if abs(target - array[0]) < abs(target - array[1]):
                return array[0]
            else:
                return array[1]


        midpoint = int(len(array) / 2)
        # second sort-of base case. If list split and target is between end of
        # first list and beginning of second, then one of them is the closest.
        if target > array[midpoint] and target < array[midpoint+1]:
            if abs(target - array[midpoint]) < abs(target - array[midpoint+1]):
                return array[midpoint]
            else:
                return array[midpoint + 1]

        # another base case
        if target >= array[-1]:
            return array[-1]
        elif target <= array[0]:
            return array[0]

        # standard binary search
        if target > array[midpoint]:
            # recurse on second half
            return self.bin_search(target, array[midpoint:])
        elif target < array[midpoint]:
            # recurse on first half
            return self.bin_search(target, array[:midpoint])
        elif target == array[midpoint]:
            return array[midpoint]


# time limit exceeded. Passed 74 of 125 test cases.


# sorts input O(nlogn), then iterates through each item in outer loop
# then each item in inner loop (O(n^2)), then for final target val, use binary
# search (O(logn)). Overall alg O(nlogn + n^2*logn) = O(n^2).
