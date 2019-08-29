"""
https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

Example 1:
    Input: 3
    Output: "III"

Example 2:
    Input: 4
    Output: "IV"

Example 3:
    Input: 9
    Output: "IX"

Example 4:
    Input: 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.

Example 5:
    Input: 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution:
    # def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        if num > 1000 and num < 4000:
            roman = 'M' * num/1000
            return roman + Solution.intToRoman(num - num/1000)
        elif num >= 900:
            roman = 'CM'
            return roman + Solution.intToRoman(num - 900)
        elif num >= 500:
            roman = 'D'
            return roman + Solution.intToRoman(num - 500)
        elif num >= 400:
            roman = 'CD'
            return roman + Solution.intToRoman(num - 400)
        elif num >= 100:
            roman = 'C' * num/100
            return roman + Solution.intToRoman(num - num/100)
        elif num >= 90:
            roman = 'XC'
            return roman + Solution.intToRoman(num - 90)
        elif num >= 50:
            roman = 'L'
            return roman + Solution.intToRoman(num - 50)
        elif num >= 40:
            roman = 'XL'
            return roman + Solution.intToRoman(num - 40)
        elif num >= 10:
            roman >= 'X' * num/10
            return roman + Solution.intToRoman(num - num/10)



        elif num == 0:
            roman = ''
            return roman
        elif num > 1 and num < 4:
            roman = 'I'*num
            return roman
        elif num == 4:
            roman = 'IV'
            return roman
        elif num > 4 and num < 9:
            roman = 'V' + 'I'*(num-5)
            return roman
        elif num == 9:
            roman = 'IX'
            return roman
        elif num > 9:
            roman = 'X'
            return roman + Solution.intToRoman()





        #
