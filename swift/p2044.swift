class Solution {
    func countMaxOrSubsets(_ nums: [Int]) -> Int {
        var maxOr = 0

        // Calculate the maximum OR value possible
        for num in nums {
            maxOr |= num
        }

        // Helper function to perform backtracking
        func backtrack(_ i: Int, _ currOr: Int) -> Int {
            if i == nums.count {
                return currOr == maxOr ? 1 : 0
            }

            
            return (
                // Include nums[i] in the subset
                backtrack(i + 1, currOr | nums[i]) +
                
                // Exclude nums[i] from the subset
                backtrack(i + 1, currOr))
        }

        // Start backtracking from the 0th element
        return backtrack(0, 0)
    }
}