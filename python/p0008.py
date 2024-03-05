class Solution:

  def myAtoi(self, s: str) -> int:
    i = 0
    numbers = []

    # Skip leading whitespaces
    while i < len(s) and s[i] == ' ':
      i += 1

    # Check for optional sign
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
      numbers.append(s[i])
      i += 1

    # Accumulate digits
    while i < len(s) and s[i].isdigit():
      numbers.append(s[i])
      i += 1

    # Check if any digits were found
    if len(numbers) == 0:
      return 0  # No valid digits found

    # Handle case where only sign character is present
    if len(numbers) == 1 and not numbers[0].isdigit():
      return 0

    # Convert numbers list to integer
    ans = int(''.join(numbers))

    # Check for overflow
    if ans > 2**31 - 1:
      return 2**31 - 1
    elif ans < -2**31:
      return -2**31
    else:
      return ans
