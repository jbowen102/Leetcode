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

# Check for number that isn't between 1 and 9.


class SudokuUnit:
    def __init__(self):
        self.entries = {}

    def fill_num(self, num):
        if self.entries.get(num):
            return True
        else:
            self.entries[num] = True
            return False

class Row(SudokuUnit):
    pass

class Col(SudokuUnit):
    pass

class Block(SudokuUnit):
    pass

# class SudokuBoard():
#     def __init__

class FullBoard():
    def __init__(self):
        self.all_rows = {}
        self.all_cols = {}
        self.all_blocks = {}
        for x in range(9):
            self.all_rows[x] = Row()
            self.all_cols[x] = Col()
            self.all_blocks[x] = Block()

    def get_row(self, row_num):
        return self.all_rows.get(row_num)

    def get_col(self, col_num):
        return self.all_cols.get(col_num)

    def get_block(self, row_num, col_num):
        block_num = 3 * int(row_num / 3) + int(col_num / 3)
        return self.all_blocks.get(block_num)

    def add_val(self, row_num, col_num, str_value):
        if str_value == '.':
            # Handle blanks on the board.
            return False
        else:
            value = int(str_value)

        Row = self.get_row(row_num)
        filled = Row.fill_num(value)
        if filled:
            return True

        Col = self.get_col(col_num)
        filled = Col.fill_num(value)
        if filled:
            return True

        Block = self.get_block(row_num, col_num)
        filled = Block.fill_num(value)
        if filled:
            return True

        return False


class Solution():
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):

        # initialize objects to store each row and each block.
        # while reading in board, populate objects, and if repitition found within
        # a row or block, return False immediately.

        Board = FullBoard()

        for row_num, row in enumerate(board):
            for entry_num, str_value in enumerate(row):
                conflict = Board.add_val(row_num, entry_num, str_value)
                if conflict:
                    return False

        return True


input_board_good = [
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

input_board_bad = [
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

input_board_bad2 = [
  ["1","3",".",".","7",".",".",".","1"],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


input_board_bad3 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  ["5",".",".",".","8",".",".","7","9"]
]

input_board_bad4 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".","5","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

input_board_bad5 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".","8","7","9"]
]

input_board_bad6 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".","6",".","8",".",".","7","9"]
]

# Accepted on first submission. Faster than 82.6%. Less mem than 100%.
