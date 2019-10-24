"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

[LC0042_RainTrap.png]

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    # def trap(self, height: List[int]) -> int:
    def trap(self, height):
        tallest = max(height)

        first_tallest = height.index(tallest)
        section_a = height[:first_tallest+1]
        print("Section A: %s" % section_a)

        # the max might occur more than once, but it doesn't matter.
        reverse_list = height[::-1]
        section_b = reverse_list[:-first_tallest]
        print("Section B: %s" % section_b)

        # if there are two instances of the max value above, there will be a middle section.
        # It can be safely treated as a part of either section a or b.

        # if tallest block occurs at the beginning or end, you get a one-block section.

        for section in [section_a, section_b]:
            for block_ht in section:



# test case 1: [1, 0, 1]
# test case 2: [2, 0, 2]
# test case 3: [1, 0, 2]
# test case 4: [2, 0, 1]
# test case 5: [1, 0, 2, 1]
# test case 5: [1, 0, 2, 0, 1]
