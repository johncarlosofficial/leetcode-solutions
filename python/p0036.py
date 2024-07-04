from typing import List
from collections import defaultdict

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize dictionaries to track seen numbers in rows, columns, and squares
    rows = defaultdict(set)
    columns = defaultdict(set)
    squares = defaultdict(set)

    # Iterate over each cell in the 9x9 Sudoku board
    for r in range(9):
      for c in range(9):
        # Skip empty cells
        if board[r][c] == ".":
          continue

        # Check if the number is already seen in the current row, column, or 3x3 square
        if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r // 3, c // 3)]:
          return False  # If duplicate is found, Sudoku is invalid

        # Add the number to the respective row, column, and square sets
        rows[r].add(board[r][c])
        columns[c].add(board[r][c])
        squares[(r // 3, c // 3)].add(board[r][c])

    return True  # If no duplicates are found, Sudoku is valid
