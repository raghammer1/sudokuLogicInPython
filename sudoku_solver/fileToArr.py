def fileReader(file):
    with open(file) as f:
        # width, height = [int(x) for x in next(f).split()]
        sudoku = []
        for line in f:
            sudoku.append([int(x) for x in line.split()])
    print(sudoku)
    return sudoku
