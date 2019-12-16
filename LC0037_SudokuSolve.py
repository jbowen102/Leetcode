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
        # https://docs.python.org/3/tutorial/datastructures.html#sets
        self.potentials = set("123456789")
        self.Cells = []

    def add_cell(self, Cell):
        self.Cells.append(Cell)

    def get_potentials(self):
        return self.potentials

    def update_potentials(self, val_to_remove):
        self.potentials = self.potentials - set(val_to_remove)

        # update children w/ new potentials.
        for Cell in self.Cells:
            Cell.update_potentials(val_to_remove)

class Row(SudokuUnit):
    pass

class Col(SudokuUnit):
    pass

class Block(SudokuUnit):
    pass


class Cell():
    def __init__(self, row_num, col_num, ParentBoard, cell_value=False):
        self.row_num = row_num
        self.col_num = col_num

        ParentRow = ParentBoard.get_row(row_num)
        ParentCol = ParentBoard.get_col(col_num)
        ParentBlock = ParentBoard.get_block(row_num, col_num)

        self.Parents = [ParentRow, ParentCol, ParentBlock]
        self.Board = ParentBoard

        if cell_value:
            self.set_val(cell_value)
        else:
            self.value = False
            self.potentials = ParentRow.get_potentials() & ParentCol.get_potentials() & ParentBlock.get_potentials()

    def get_row_num(self):
        return self.row_num

    def get_col_num(self):
        return self.col_num

    def set_val(self, new_val_str):
        self.value = new_val_str
        self.Board.fill_in(self, new_val_str)   # Propagate change to board array.
        self.potentials = set()

        # update parents
        for Parent in self.Parents:
            Parent.update_potentials(self.value)

    def update_potentials(self, val_to_remove):
        # cell may not have val_to_remove in its potentials due to ruling out
        # by a different parent.
        if val_to_remove in self.potentials:
            self.potentials = self.potentials - set(val_to_remove)

            if len(self.potentials) == 1:
                # When there's only one possible num left, give cell this val.
                val_to_assign = self.potentials.pop()
                self.set_val(val_to_assign)
                # set_val will update parents


class FullBoard():
    def __init__(self, board):

        # Must modify board in place.
        self.board_array = board

        # initialize empty board.
        self.all_rows = {}
        self.all_cols = {}
        self.all_blocks = {}
        self.all_cells = {}

        # Generate all units.
        for x in range(9):
            self.all_rows[x] = Row()
            self.all_cols[x] = Col()
            self.all_blocks[x] = Block()

        # Generate all cells.
        # Have to loop twice so all rows, cols, and blocks are generated first.
        for row_num in range(9):
            for col_num in range(9):
                CurrentRow = self.get_row(row_num)
                CurrentCol = self.get_col(col_num)
                CurrentBlock = self.get_block(row_num, col_num)

                index = 9 * row_num + col_num
                self.all_cells[index] = Cell(row_num, col_num, self)

                # Associate cell to units.
                CurrentRow.add_cell(self.all_cells[index])
                CurrentCol.add_cell(self.all_cells[index])
                CurrentBlock.add_cell(self.all_cells[index])


    def get_array(self):
        return self.board_array

    def fill_in(self, Cell, val_str):
        self.board_array[Cell.get_row_num()][Cell.get_col_num()] = val_str

    def get_row(self, row_num):
        return self.all_rows.get(row_num)

    def get_col(self, col_num):
        return self.all_cols.get(col_num)

    def get_block(self, row_num, col_num):
        block_num = 3 * int(row_num / 3) + int(col_num / 3)
        return self.all_blocks.get(block_num)

    def get_cell(self, row_num, col_num):
        cell_num = 9 * row_num + col_num
        return self.all_cells.get(cell_num)

    def add_val(self, row_num, col_num, str_value):

        if str_value != '.':
            # Blanks do not have an effect on rest of board.
            Cell = self.get_cell(row_num, col_num)
            Cell.set_val(str_value)


class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        # build empty board
        Board = FullBoard(board)

        # Enter each value, with the objects updating each other as it goes.
        # Array can change during each iteration, so can't load intiial state
        # of row or col into mem and use enumerate. Must re-index array each time.
        row_num = 0
        while True:

            col_num = 0
            while True:
                str_value = Board.get_array()[row_num][col_num]
                Board.add_val(row_num, col_num, str_value)

                col_num += 1
                if col_num > 8:
                    break

            row_num += 1
            if row_num > 8:
                break

# works on test case 1 but not 2. Leaves board unchanged.

input_board1 = [
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

# input_board1 solution:
# ['5', '3', '4', '6', '7', '8', '9', '1', '2']
# ['6', '7', '2', '1', '9', '5', '3', '4', '8']
# ['1', '9', '8', '3', '4', '2', '5', '6', '7']
# ['8', '5', '9', '7', '6', '1', '4', '2', '3']
# ['4', '2', '6', '8', '5', '3', '7', '9', '1']
# ['7', '1', '3', '9', '2', '4', '8', '5', '6']
# ['9', '6', '1', '5', '3', '7', '2', '8', '4']
# ['2', '8', '7', '4', '1', '9', '6', '3', '5']
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']

input_board2 = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]
