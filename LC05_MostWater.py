"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above [pic] vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

# First approach is exhaustive enumeration, but that runs in N^2 time.

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, heights):
        max_water = 0
        for posf, heightf in enumerate(heights):
            for posl, heightl in enumerate (heights[posf+1:]):
                abs_posl = posf+1 + posl    # posl always starts at 0
                water_area = min(heightf, heightl) * (abs_posl - posf)
                # print(water_area)
                if water_area > max_water:
                    max_water = water_area
        return max_water

# Need to review section in Algorithms book about evaluating combinations of items in a list.
