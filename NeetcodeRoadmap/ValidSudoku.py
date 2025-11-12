def isValidSudoku(board) -> bool:
    # hash set rows an cols
    columns = [[] for i in range(0, len(board))]
    cols = {}

    # create cols array
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            columns[i].append(board[j][i])

    # check rows and cols ---
    # hash set rows
    for index, row in enumerate(board):
        rows = set()
        for val in row:
            if val in rows and val != ".":
                return False
            rows.add(val)

    # hash set cols
    for index, col in enumerate(columns):
        cols = set()
        for val in col:
            if val in cols and val != ".":
                return False
            cols.add(val)
    # ---

    # check individual grid
    for i in range(0, 3):
        for j in range(0, 3):
            square = set()
            # check grid vals in set
            for k in range(0, 3):
                for l in range(0, 3):
                    value = board[k + (3 * i)][l + (3 * j)]
                    if value in square and value != ".":
                        return False
                    square.add(value)
    # else no contradictions found
    return True
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))