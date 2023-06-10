# This function will print the origin unfilled sudoku
# and the final filled sudoku
def printer(sudoku, originalSudoku):
    print("\n -----------------------")
    for i in range(9):
        for j in range(9):
            if j == 0:
                print("|", end=" ")
            if originalSudoku[i][j] == 0:
                print(sudoku[i][j], end=" ")
            else:
                print("\033[1m" + str(sudoku[i][j]) + "\033[0m", end=" ")
            if (j - 2) % 3 == 0:
                print("|", end=" ")
        if (i - 2) % 3 != 0:
            print()
        else:
            print("\n -----------------------")
    print()
