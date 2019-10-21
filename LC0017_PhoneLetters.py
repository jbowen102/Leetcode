"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

[LC0017_PhoneLetters.png]


Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in
any order you want.
"""

class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:

    def init(self):
        self.key_map = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno',
                        7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        self.output_list = []

    def letterCombinations(self, digits):
        if not digits:
            return ''

        else:
            for letter in self.key_map[digits[0]]:
                self.output_list.append(letter + self.letterCombinations(digits[1:]))


        return self.output_list
