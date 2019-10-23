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
        # get to the first concave section
        last_block = height[0]
        n = 1
        block = height[n]
        block_slope = block - last_block

        while block_slope > 0:
            print("Burn block %i" % block)
            last_block = block
            n += 1
            block = height[n]
            block_slope = block - last_block

# could initialize differently by starting main loop with last_block = 0.
# That way no water could be held, and nothing would be added to count.
# Change after finishing main loop, so it can be adapted.


        print("First block after initialization: %s" % block)


        # if "slope" is downward, start keeping track of descent.
        # when slope switches to upward, count how many steps up it goes <= how many it went down.
        # when slope switches from upward to downward, cut off the count and start a new one.

        for block in height[n:]:
            block_slope = block - last_block
            print("block: %s" % block)
            print("block slope: %i" % block_slope)
            last_block = block

# need to handle convex part at end. Could naturally be handled by loop starting
# count but never finishing because slope never goes positive again.




# test case 1: [1, 0, 1]
# test case 2: [2, 0, 2]
# test case 3: [1, 0, 2]
# test case 4: [2, 0, 1]
# test case 5: [1, 0, 2, 1]
# test case 5: [1, 0, 2, 0, 1]
