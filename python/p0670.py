class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits, so we can swap them easily.
        num = list(str(num))  
        
        # Create a list to store the maximum digit found from each position to the right.
        # The list will hold tuples (max_digit, index_of_max_digit).
        # Initialize it with '0's, which will be replaced later.
        max_right = ["0"] * len(num)
        
        # Variables to keep track of the maximum digit and its index as we scan the number from right to left.
        max_digit = "0"
        max_index = 0

        # Traverse the digits of the number from right to left.
        # The goal is to record the largest digit to the right of each position.
        for i in range(len(num) - 1, -1, -1):
            # If the current digit is greater than the recorded maximum digit, update the max_digit and max_index.
            if num[i] > max_digit:
                max_digit = num[i]
                max_index = i
            
            # Store the largest digit seen so far and its index at each position.
            max_right[i] = (max_digit, max_index)

        # Traverse the digits of the number again from left to right.
        for i in range(len(num)):
            # If the current digit is smaller than the maximum digit to the right, perform the swap.
            if num[i] < max_right[i][0]:
                # Swap the current digit with the largest digit found to the right.
                num[i], num[max_right[i][1]] = num[max_right[i][1]], num[i]
                # After swapping, break out of the loop as we can only swap once.
                break

        # Convert the list of digits back to a single integer and return it.
        return int("".join(num))
