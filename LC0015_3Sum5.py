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


        n = 0
        while n < len(nums):
            item = nums[n]
            # print("\tnums: %s" % nums)
            # print("%s_%s" % (n, item))
            # The number's position is stored in a list as the value.
            # Since duplicate nums are allowed, a list is used.
            if not item_dict.get(item):
                item_dict[item] = [n]
                n += 1
            elif ((item != 0 and len(item_dict[item]) >= 2) or
                 (item == 0 and len(item_dict[item]) >= 3)):
                # If a number repeats more than twice (except zero), it can be
                # removed from the list and not appended to dict.
                del(nums[n])
                # Don't advance list index since an item has been removed.
            else:
                item_dict[item] += [n]
                n += 1

        # print("Processed nums: %s" % str(nums))

        # diagnostics:
        # items = sorted(item_dict.keys())
        # print("item_dict: ")
        # for n in items:
        #     print(str(n) + ": " + str(item_dict[n]))
        # input()

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
                    #     print("\t\tSoln set already contains " + str(triple))
        return soln_triples


    # Still an n^2 implementation

    # What could speed it up?
    # Pre-processing step(s)? Sort array first? Split list into <0 and >0 halves?
    # Look for a zero in the list and if it exists then the problem reduces to two-sum.
