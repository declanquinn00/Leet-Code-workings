def exist(board, word):
    res = []
    subarray = []
    row_len = len(board[0])
    col_len = len(board)

    def backtrack(position, grid, i):
        if i >= len(word):
            if "".join(subarray.copy()) == word:
                res.append("".join(subarray.copy()))
            else:
                return

        # backtracking step
        subarray.append(board[position[0]][position[1]])

        # check up
        if position[0] < row_len and position[0] >= 0:
            if position[1] - 1 < row_len and position[1] - 1 >= 0:
                if not grid[position[0]][position[1] - 1]:
                    new_position = (position[0], position[1] - 1)
                    grid[new_position[0]][new_position[1]] = True
                    backtrack(new_position, grid, i + 1)
                    grid[new_position[0]][new_position[1]] = False

        # check down
        if position[0] < row_len and position[0] >= 0:
            if position[1] + 1 < row_len and position[1] + 1 >= 0:
                if not grid[position[0]][position[1] + 1]:
                    new_position = (position[0], position[1] + 1)
                    grid[new_position[0]][new_position[1]] = True
                    backtrack(new_position, grid, i + 1)
                    grid[new_position[0]][new_position[1]] = False

        # check left
        if position[0] - 1 < col_len and position[0] - 1 >= 0:
            if position[1] < col_len and position[1] >= 0:
                if not grid[position[0] - 1][position[1]]:
                    new_position = (position[0] - 1, position[1])
                    grid[new_position[0]][new_position[1]] = True
                    backtrack(new_position, grid, i + 1)
                    grid[new_position[0]][new_position[1]] = False

        # check right
        if position[0] + 1 < col_len and position[0] + 1 >= 0:
            if position[1] < col_len and position[1] >= 0:
                if not grid[position[0] + 1][position[1]]:
                    new_position = (position[0] + 1, position[1])
                    grid[new_position[0]][new_position[1]] = True
                    backtrack(new_position, grid, i + 1)
                    grid[new_position[0]][new_position[1]] = False

        subarray.pop()
        if position[0] >= row_len:
            position[0] = 0
            position[1] += 1
        if position[1] >= col_len:
            return
        new_position = (position[0],position[1])
        grid[new_position[0]][new_position[1]] = True
        backtrack(new_position, grid, 0)
        grid[new_position[0]][new_position[1]] = False


    grid = [[False] * row_len for _ in range(0, col_len)]
    backtrack((0, 0), grid, 0)
    if res == word:
        return True
    else:
        return False


board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"
print(exist(board, word))