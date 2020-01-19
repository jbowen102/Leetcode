"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
    Input: 2.00000, 10
    Output: 1024.00000

Example 2:
    Input: 2.10000, 3
    Output: 9.26100

Example 3:
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""

class Solution:
    # def myPow(self, x: float, n: int) -> float:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 1:
            return 1 / self.myPow(x, -n)
        elif (n % 2) == 0:
            return self.myPow(x*x, n/2)
        elif (n % 2) == 1:
            return x * self.myPow(x, n-1)



# back to using recusion, but now faster because exponent gets divided.

# tests
mysol = Solution()

x = 0.00001
n = 2147483647
print(mysol.myPow(x, n))
# passed
