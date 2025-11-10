# could have worked out the next row length better!
def generate(numRows: int):
    rows = []

    # edge cases
    if numRows == 1:
        return [[1]]

    if numRows == 0 or numRows == None:
        return [[]]

    # do first row
    if numRows > 1:
        row = [1]
        rows.append(row)

        for i in range(1, numRows):
            next_row_length = i + 1
            next_row = []

            # append first edge val
            next_val = rows[i - 1][0]
            next_row.append(next_val)
            # append middle vals
            for j in range(0, next_row_length - 2):
                next_val = rows[i - 1][0+j] + rows[i - 1][0 + j + 1]
                next_row.append(next_val)
            # append last edge val
            next_val = rows[i - 1][next_row_length - 2]
            next_row.append(next_val)
            # append the next row
            rows.append(next_row)

    return rows
rows = generate(5)
print(rows)