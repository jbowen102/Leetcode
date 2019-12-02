"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.

"""

class SudokuUnit:
    def __init__(self):
        self.entries = {}

    def fill_num(self, num):
        if self.entries.get(num):
            return False
        else:
            self.entries[num] = True
            return True

class Row(SudokuUnit):
    pass

class Block(SudokuUnit):
    pass


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):

        # initialize objects to store each row and each block.
        # while reading in board, populate objects, and if repitition found within
        # a row or block, return False immediately.

        BlockTL = Block()
        BlockTM = Block()
        BlockTR = Block()
        BlockCL = Block()
        BlockCM = Block()
        BlockCR = Block()
        BlockBL = Block()
        BlockBM = Block()
        BlockBR = Block()

        Row1 = Row()
        Row2 = Row()
        Row3 = Row()
        Row4 = Row()
        Row5 = Row()
        Row6 = Row()
        Row7 = Row()
        Row8 = Row()
        Row9 = Row()

        for row in board[:3]:
            for num in row[:3]:
                # add to both row object and top left block object
                Row1.fill_num(num)
                BlockTL.fill_num(num)

            for num in row[3:6]:
                # add to both row object and top middle block object
                Row2.fill_num(num)
                BlockTM.fill_num(num)

            for num in row[6:9]:
                # add to both row object and top right block object
                Row3.fill_num(num)
                BlockTR.fill_num(num)

        for row in board[3:6]:
            for num in row[:3]:
            # for cols 1-3:
                # add to both row object and center left block object
                Row4.fill_num(num)
                BlockCL.fill_num(num)

            for num in row[3:6]:
            # for cols 4-6:
                # add to both row object and center middle block object
                Row5.fill_num(num)
                BlockCM.fill_num(num)

            for num in row[6:9]:
            # for cols 7-9:
                # add to both row object and center right block object
                Row6.fill_num(num)
                BlockCR.fill_num(num)

        for row in board[6:9]:
            for num in row[:3]:
            # for cols 1-3:
                # add to both row object and bot left block object
                Row7.fill_num(num)
                BlockBL.fill_num(num)

            for num in row[3:6]:
            # for cols 4-6:
                # add to both row object and bot middle block object
                Row8.fill_num(num)
                BlockBM.fill_num(num)

            for num in row[6:9]:
            # for cols 7-9:
                # add to both row object and bot right block object
                Row9.fill_num(num)
                BlockBR.fill_num(num)
