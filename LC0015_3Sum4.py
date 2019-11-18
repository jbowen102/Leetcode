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

        # Read all items into a dict for quick checking later as each 2sum computed.
        # Dict will be checked for the negative complement to the 2sum.
        item_dict = {}
        for n, item in enumerate(nums):
            # The number's position is stored in a list as the value.
            # Since duplicate nums are allowed, a list is used.
            if not item_dict.get(item):
                item_dict[item] = [n]
            else:
                item_dict[item] += [n]

        # diagnostics:
        # items = sorted(item_dict.keys())
        # print("item_dict: ")
        # for n in items:
        #     print(str(n) + ": " + str(item_dict[n]))

        for i, first in enumerate(nums):
            # print(str(i) + '_' + str(first))
            for j, second in enumerate(nums[i+1:]):
                # print('\t' + str(j) + '_' + str(second))
                neg_comp = -(first + second)
                m = i + j + 1           # Global list index of the second number.

                # Find if a copy of the negative complement still exists in the array.
                if item_dict.get(neg_comp):
                    locs = item_dict.get(neg_comp).copy()
                    # print("\t\tlocs for neg_comp %s: %s" % (str(neg_comp), str(locs)))

                    # If one is found, eliminate duplicates representing first and second
                    # picks from this iteration.
                    if i in locs:
                        locs.remove(i)
                    if m in locs:
                        locs.remove(m)
                # else:
                    # print("\t\tComplement %s not found in table." % neg_comp)

                # If locs still contains an index, then it can be used in the triple.
                # Have to re-test the existence of the unaltered list in case
                # locs ends up not being assigned yet.
                if item_dict.get(neg_comp) and locs:
                    triple = tuple(sorted([first, second, neg_comp]))
                    # sort each triplet, then add each to a hash table.
                    # Don't store if a duplicate triple already exists.
                    if not soln_triples_dict.get(triple):
                        soln_triples.append(list(triple))
                        soln_triples_dict[triple] = True
                        # print("\t\tAdded %s to soln set." % str(triple))
                    # else:
                        # print("\t\tSoln set already contains " + str(triple))
        return soln_triples


    # n^2 implementation

    # failed on huge list of zeros. Should pre-process input list and eliminate
    # any numbers that repeat more than thrice.


    # What can be done with hash tables to solve faster?
    # Dynamic programming? Are there overlapping sub-problems?
    # Pre-processing step(s)? Sort array first? Split list into <0 and >0 halves?
    # Look for a zero in the list and if it exists then the problem reduces to two-sum.
    # Remove any duplicates of numbers >= three times. Leave only max of two instances.
    # apply hash table twice somehow?
