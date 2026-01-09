
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    first = False

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                # set col
                matrix[0][col] = 0
                if row > 0:
                    matrix[row][0] = 0
                else:
                    # set row
                    first = True

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for j in range(0, len(matrix)):
            matrix[j][0] = 0

    if first:
        for i in range(0, len(matrix[0])):
            matrix[0][i] = 0

setZeroes([[1],[0],[3]])