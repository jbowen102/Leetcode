"""
Given an array nums of n integers, are there elements a, b, c in nums such that
 a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):

        soln_triples = []
        soln_triples_dict = {}

        for i, first in enumerate(nums):
            # print(str(i) + '_' + str(first))
            for j, second in enumerate(nums[i+1:]):
                # print('\t' + str(j) + '_' + str(second))
                for k, third in enumerate(nums[i+1:][j+1:]):
                    # print('\t\t' + str(i) + '_' + str(third))
                    if first+second+third == 0:
                        triple = tuple(sorted([first, second, third]))
                        # sort each triplet, then add each to a hash table.
                        # Don't store if a duplicate triple already exists.
                        if not soln_triples_dict.get(triple):
                            soln_triples.append(list(triple))
                            soln_triples_dict[triple] = True
        return soln_triples


    # Naive implementation - n^3 complexity.
    # Won't pass all test cases on Leetcode because of time limit exceeded.
