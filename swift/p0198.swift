class Solution {
    func rob(_ nums: [Int]) -> Int {
        // Handle edge cases for small arrays
        if nums.count == 1 {
            return nums[0]
        }
        
        if nums.count == 2 {
            return max(nums[0], nums[1])
        }
        
        var twoHousesAgo = 0  // Max money robbed up to two houses ago
        var previousHouse = 0  // Max money robbed up to the last house
        
        // Iterate over the array using index
        for i in 0..<nums.count {
            let currentMax = max(previousHouse, twoHousesAgo + nums[i])  // Max if robbing current house
            twoHousesAgo = previousHouse  // Update for the next iteration
            previousHouse = currentMax  // Update for the next iteration
        }
        
        return previousHouse  // Final maximum amount robbed
    }
}
