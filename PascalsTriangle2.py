rowIndex = 3
def ans(rowIndex):
    numrows = rowIndex
    if rowIndex < 0 or None:
        return None
    # create first row
    if rowIndex == 0:
        return [1]
    # create all other rows
    rows = [[1]]
    for i in range(1, rowIndex + 1):
        row = []
        rowLength = i + 1
        # create left edge
        row.append(1)
        # create middle
        for j in range(1, rowLength - 1):
            row.append((rows[i - 1][j - 1] + rows[i - 1][j]))
        # create right edge
        row.append(1)

        rows.append(row)
    return row

row = ans(3)
print(row)
