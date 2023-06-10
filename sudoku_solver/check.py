# This function checks if the sudoku has the current num in the current column, row or 3x3 box
def checker(sudoku, thisRow, thisColumn, num):

    if unusedInColumn(num, sudoku, thisColumn) == False or unusedInRow(num, sudoku, thisRow) == False:
        return False

    thisRow = thisRow - thisRow % 3
    thisColumn = thisColumn - thisColumn % 3

    return box_checker(sudoku, thisRow, thisColumn, num)


def box_checker(sudoku, thisRow, thisColumn, num):
    for i in range(thisRow, thisRow + 3, 1):
        for j in range(thisColumn, thisColumn + 3, 1):
            if sudoku[i][j] == num:
                return False
    return True


def unusedInColumn(num, sudoku, thisColumn):
    for i in range(9):
        if sudoku[i][thisColumn] == num:
            return False


def unusedInRow(num, sudoku, thisRow):
    for i in range(9):
        if sudoku[thisRow][i] == num:
            return False
