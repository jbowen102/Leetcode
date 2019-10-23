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

class Solution(object):
    # def letterCombinations(self, digits: str) -> List[str]:

    def __init__(self):
        self.key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        output_list = []
        # print('digits: %s' % digits)

        if digits:
            # recurse and get all combinations of letters later in the sequence.
            lower_level_list = self.letterCombinations(digits[1:])

            letters = self.key_map[digits[0]]
            for letter in letters:
                # print('\tletter %s from set %s' % (letter, letters))
                if lower_level_list:
                    for existing_string in lower_level_list:
                        # print('\tadding %s to string %s' % (letter, existing_string))
                        output_list.append(letter + existing_string)
                else:
                    # print('\tappending letter %s by itself' % letter)
                    output_list.append(letter)

        return output_list

# Successfully submitted
