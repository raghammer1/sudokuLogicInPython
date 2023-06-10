from print import printer
from sudokuSolver import solver
from fileToArr import fileReader
from os.path import exists
import numpy as np
import random

def worker():
    file = str(input("Please enter the file path: "))

    fileExists = exists(file)

    if fileExists == False:
        print("The given file " + file + " does not exist")
        exit()

    sudoku = fileReader(file)

    print("\n\nThis is the original unsolved sudoku grid")
    originalSudoku = fileReader(file)


    printer(sudoku, originalSudoku)


    if solver(sudoku, 0, 0):
        print("\nThis is the solved sudoku grid")
        printer(sudoku, originalSudoku)
        randomnum1 = random.randint(0, 1000)
        randomnum2 = random.randint(0, 1000)
        randomnum3 = random.randint(0, 100000)
        rand = str(randomnum1 * randomnum2 + randomnum3)
        np.savetxt("solvedSudoku"+rand+".txt",sudoku)
        return "solvedSudoku"+rand+".txt"

    else:
        print("There was NO possible solution for this sudoku")

worker()