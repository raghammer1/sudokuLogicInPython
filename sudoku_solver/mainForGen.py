from check import unusedInRow
from check import box_checker, unusedInColumn, unusedInRow
from print import printer
import random


def fillDiag():
    i = 0
    while i < 9:
        fillBox(i, i)
        i = i + 3


def fillBox(thisRow, thisCol):
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            num = random.randint(1, 10)
            while unUsedInBox(thisRow, thisCol, num) == False:
                sudoku[thisRow][thisCol] = num


def unUsedInBox(rowStart, colStart, num):
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if sudoku[rowStart + i][colStart + j] == num:
                return False
            j += 1
        i += 1

    return True


def fillRemaining():
    i = 0
    j = 3

    if j >= 9 and i < 9 - 1:
        i = i + 1
        j = 0

    if i >= 9 and j >= 9:
        return True

    if i < 3:
        if j < 3:
            j = 3

    elif i < 9 - 3:
        if j == (i / 3) * 3:
            j = j + 3

    else:
        if j == 9 - 3:
            i = i + 1
            j = 0
            if i >= 9:
                return True

    for num in range(1, 10, 1):
        if CheckIfSafe(i, j, num):
            sudoku[i][j] = num
            if fillRemaining(i, j + 1):
                return True

            sudoku[i][j] = 0

    return False


def CheckIfSafe(i, j, num):
    return (
        unusedInRow(num, sudoku, i)
        and unusedInColumn(num, sudoku, j)
        and unUsedInBox(i - i % 3, j - j % 3, num)
    )


def removeDigits(diff):
    while diff != 0:
        cellNum = random.randint(0, 10)

        i = int(cellNum / 9)
        j = cellNum % 9

        if j != 0:
            j = j - 1

        if sudoku[i][j] != 0:
            diff -= 1
            sudoku[i][j] = 0


col = row = 9

sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

difficulty = str(input("Please enter your difficulty level Hard, Medium or Easy: "))
if difficulty.lower() == "easy":
    difficulty_num = 20
elif difficulty.lower() == "medium":
    difficulty_num = 25
elif difficulty.lower() == "hard":
    difficulty_num = 30
else:
    difficulty_num = 20

fillDiag()
fillRemaining()
removeDigits(difficulty_num)
printer(sudoku, sudoku)

# NO random generator function is used here
