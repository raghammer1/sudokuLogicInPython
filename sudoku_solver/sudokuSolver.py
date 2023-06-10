from check import checker


def solver(sudoku, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        col = 0
        row += 1

    if sudoku[row][col] > 0:
        return solver(sudoku, row, col + 1)

    for num in range(1, 10, 1):
        if checker(sudoku, row, col, num):
            sudoku[row][col] = num

            if solver(sudoku, row, col + 1):
                return True
        sudoku[row][col] = 0

    return False
