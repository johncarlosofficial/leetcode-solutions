class Solution:

  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
      return s

    # Create a list to hold the characters for each row
    rows = [''] * numRows
    # Initialize the direction to move in the zigzag pattern (-1 for up, 1 for down)
    direction = -1
    # Initialize the current row index
    row = 0

    for char in s:
      rows[row] += char
      # If we're at the first or last row, change the direction
      if row == 0 or row == numRows - 1:
        direction *= -1
      # Move to the next row based on the direction
      row += direction

    # Concatenate all rows to form the zigzag pattern
    return ''.join(rows)
