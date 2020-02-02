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
        else:
            return x * self.myPow(x, n-1)



# tests
mysol = Solution()

x = 2.10000
n = 3
print(mysol.myPow(x, n))

# failed this case:
x = 1.00001
n = 123456