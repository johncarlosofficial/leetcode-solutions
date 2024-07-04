/**
 * @param {character[][]} board
 * @return {boolean}
 */
export var isValidSudoku = function (board) {
  // Initialize dictionaries to track seen numbers in rows, columns, and squares
  const rows = Array.from({ length: 9 }, () => new Set());
  const columns = Array.from({ length: 9 }, () => new Set());
  const squares = Array.from({ length: 9 }, () => new Set());

  // Iterate over each cell in the 9x9 Sudoku board
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      // Skip empty cells
      if (board[r][c] === ".") continue;

      const num = board[r][c];
      const squareIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3);

      // Check if the number is already seen in the current row, column, or 3x3 square
      if (
        rows[r].has(num) ||
        columns[c].has(num) ||
        squares[squareIndex].has(num)
      ) {
        return false; // If duplicate is found, Sudoku is invalid
      }

      // Add the number to the respective row, column, and square sets
      rows[r].add(num);
      columns[c].add(num);
      squares[squareIndex].add(num);
    }
  }

  return true; // If no duplicates are found, Sudoku is valid
};
