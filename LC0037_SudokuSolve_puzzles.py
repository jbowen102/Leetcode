
# works on test case 1 but not 2. Makes some changes, but leaves board incomplete.

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


# Returning this - non-deterministic at this stage?:
[
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".","6",".","2",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7","9","8","6","2","4","1"],
    ["2","6","4","3","1","7","5","9","8"],
    ["1","9","8","5","2","4","3","6","7"],
    [".",".",".","8","6","3",".","2","."],
    [".",".",".","4","9","1",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]

# correct answer
[
    ["5","1","9","7","4","8","6","3","2"],
    ["7","8","3","6","5","2","4","1","9"],
    ["4","2","6","1","3","9","8","7","5"],
    ["3","5","7","9","8","6","2","4","1"],
    ["2","6","4","3","1","7","5","9","8"],
    ["1","9","8","5","2","4","3","6","7"],
    ["9","7","5","8","6","3","1","2","4"],
    ["8","3","2","4","9","1","7","5","6"],
    ["6","4","1","2","7","5","9","8","3"]
]

# possible deterministic version of input_board2:
input_board3 = [
    [".",".","9","7","4","8",".",".","2"],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    ["6",".",".","2","7","5","9",".","."]
]


# from websudoku.com:
# program solved correctly.
input_board5 = [
    ["7",".","2",".",".","6",".",".","1"],
    ["9",".",".",".","5","2",".",".","8"],
    [".","5",".",".",".",".","2","7","."],
    [".","7",".",".",".",".","6",".","5"],
    [".","6","1",".",".",".","7","8","."],
    ["8",".","3",".",".",".",".","9","."],
    [".","8","5",".",".",".",".","4","."],
    ["3",".",".","4","1",".",".",".","7"],
    ["2",".",".","6",".",".","8",".","3"]
]
