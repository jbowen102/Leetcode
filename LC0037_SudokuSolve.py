"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

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
Output: [filled-in puzzle]


Note:
    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.

"""


class SudokuUnit:
    def __init__(self):
        # https://docs.python.org/3/tutorial/datastructures.html#sets
        self.potentials = set("123456789")
        # self.potentials = dict([("1", 0), ("2", 0), ("3", 0), ("4", 0), ("5", 0), 
        #                         ("6", 0), ("7", 0), ("8", 0), ("9", 0)])
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
            elif len(self.potentials) == 0:
                pass
                # need to return something that indicates an upstream guess was unsuccessful

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
        cell_index = 9 * row_num + col_num
        return self.all_cells.get(cell_index)

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
        # Array can change during each iteration, so can't load initial state
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


##### TEST #####

import LC0037_SudokuSolve_puzzles as puzzles
mysol = Solution()

for row in puzzles.input_board2:
    print(row)

mysol.solveSudoku(puzzles.input_board2)

print("\n\tDeterministic Solution First-pass\n\t->\n")
for row in puzzles.input_board2:
    print(row)

# works on test case 1 but not 2. Only solves part of the board.

# Need to add code to keep track of when a cell becomes the only one in a unit
# (row, col, or block) that can possibly take on a certain value. Could be a
# dictionary in the unit w/
# {value: (possible cell, possible cell, possible cell...)} pairs.
# Need to keep track of when any given value reaches a count of one so it can
# be assigned.
# This does not solve board 2 though. Still need a mechanism to make and validate
# value guesses once board becomes (seemingly) non-determinant. Or need more
# insight into how to solve boards that reach this state.
