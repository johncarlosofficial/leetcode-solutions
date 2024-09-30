class Solution {
    func jump(_ nums: [Int]) -> Int {
        // 'result' will store the minimum number of jumps required to reach the last index
        var jumps = 0

        // 'currentStart' and 'currentEnd' represent the range of indices we can jump from
        var currentStart = 0
        var currentEnd = 0

        // We loop until 'currentEnd' reaches the last index of the array
        while (currentEnd < nums.count - 1) {
            // 'farthestJump' will track the farthest position we can reach within the current jump
            var farthestJump = 0

            // Iterate over all indices from 'currentStart' to 'currentEnd' to find the farthest jump
            for i in currentStart...currentEnd {
                // Update the farthest position we can reach from the current position 'i'
                farthestJump = max(farthestJump, nums[i] + i)
            }

            // Increase the number of jumps as we are moving to a new range
            jumps += 1

            // Move 'currentStart' to the next range (just beyond the current end)
            currentStart = currentEnd + 1

            // Update 'currentEnd' to the farthest position we can jump to
            currentEnd = farthestJump
        }

        // Return the total number of jumps required
        return jumps
    }
}
