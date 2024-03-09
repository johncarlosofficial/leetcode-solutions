from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    
    # Check rows
    for row in range(len(board)):
      my_set = set()
      for column in range(len(board[row])):
        if board[row][column].isdigit():
          if board[row][column] in my_set:
            return False
          else:
            my_set.add(board[row][column])

    # Check columns
    for row in range(len(board)):
      my_set = set()
      for column in range(len(board[row])):
        if board[column][row].isdigit():
          if board[column][row] in my_set:
            return False
          else:
            my_set.add(board[column][row])

    return True

