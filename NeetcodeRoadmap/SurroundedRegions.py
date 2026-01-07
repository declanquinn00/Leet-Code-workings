def solve(board):
    marked = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        marked.add((r, c))
        for direction in directions:
            row = r + direction[0]
            col = c + direction[1]
            if row in range(len(board)) and col in range(len(board[0])) and (row, col) not in marked and board[row][col] == "O":
                dfs(row, col)
        return

    # check all outside edge cases
    for i in range(len(board)):
        for j in range(len(board[0])):
            # check edge values
            if (i == 0 or i == len(board) - 1) and board[i][j] == "O":
                dfs(i, j)

            if (j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
                dfs(i, j)

    # change every other unmarked loc
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and not (i, j) in marked:
                board[i][j] = "X"

board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

solve(board)