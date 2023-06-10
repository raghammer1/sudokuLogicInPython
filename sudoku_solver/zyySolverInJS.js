let sudoku = [
  [2, 5, 0, 0, 3, 0, 9, 0, 1],
  [0, 1, 0, 0, 0, 4, 0, 0, 0],
  [4, 0, 7, 0, 0, 0, 2, 0, 8],
  [0, 0, 5, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 9, 8, 1, 0, 0],
  [0, 4, 0, 0, 0, 3, 0, 0, 0],
  [0, 0, 0, 3, 6, 0, 0, 7, 2],
  [0, 7, 0, 0, 0, 0, 0, 0, 3],
  [9, 0, 3, 0, 0, 0, 6, 0, 4],
];

let originalSudoku = [
  [7, 0, 0, 0, 0, 5, 0, 0, 0],
  [8, 4, 0, 0, 0, 0, 9, 0, 0],
  [2, 0, 0, 0, 4, 1, 0, 6, 0],
  [0, 0, 0, 0, 0, 0, 5, 0, 8],
  [0, 0, 5, 9, 0, 0, 0, 0, 4],
  [0, 0, 6, 2, 0, 0, 0, 1, 0],
  [0, 0, 8, 3, 0, 9, 0, 0, 6],
  [0, 1, 0, 0, 7, 0, 0, 0, 0],
  [3, 0, 0, 0, 0, 0, 0, 0, 0],
];

main();

function main() {
  if (solver(sudoku, 0, 0)) {
    // console.log('DONE');
    console.log(sudoku);
    // printed(sudoku, originalSudoku);
  } else {
    console.log('NO possible solutions');
  }
}

function solver(sudoku, row, col) {
  if (row == 8 && col == 8) {
    return true;
  }
  if (col === 9) {
    col = 0;
    row++;
  }
  if (sudoku[row][col] > 0) {
    return solver(sudoku, row, col + 1);
  }
  for (let num = 1; num < 10; num++) {
    // console.log(checker(sudoku, row, col, num));
    if (checker(sudoku, row, col, num)) {
      sudoku[row][col] = num;
      if (solver(sudoku, row, col + 1)) {
        return true;
      }
    }
    sudoku[row][col] = 0;
  }
  return false;
}

function checker(sudoku, row, col, num) {
  if (
    unusedInColumn(num, sudoku, col) == false ||
    unusedInRow(num, sudoku, row) == false
  ) {
    return false;
  }
  row = row - (row % 3);
  col = col - (col % 3);
  // console.log(row, col);
  return boxChecker(sudoku, row, col, num);
}

function unusedInColumn(num, sudoku, col) {
  for (let i = 0; i < 9; i++) {
    if (sudoku[i][col] === num) {
      return false;
    }
  }
}

function unusedInRow(num, sudoku, row) {
  for (let i = 0; i < 9; i++) {
    if (sudoku[row][i] === num) {
      return false;
    }
  }
}

function boxChecker(sudoku, row, col, num) {
  for (let i = row; i < row + 3; i++) {
    for (let j = col; j < col + 3; j++) {
      if (sudoku[i][j] === num) {
        return false;
      }
    }
  }
  return true;
}
