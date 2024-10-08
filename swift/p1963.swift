class Solution {
    func minSwaps(_ s: String) -> Int {
        var balance = 0 // Tracks the imbalance between closing and opening brackets
        var max_imbalance = 0 // Tracks the maximum imbalance

        for char in s {
            if char == "]" {
                balance += 1 // Increase imbalance when encountering a closing bracket
            } else {
                balance -= 1 // Decrease imbalance when encountering an opening bracket
            }

            // Update max_imbalance if balance goes above 0 (unbalanced closing brackets)
            max_imbalance = max(max_imbalance, balance)
        }

        // The minimum swaps needed is half the maximum imbalance (rounded up)
        return (max_imbalance + 1) / 2
    }
}