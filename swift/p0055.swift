class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        // The 'goal' represents the position we need to reach or exceed
        // Start by setting the goal to the last index of the array 'nums'
        var goal = nums.count - 1

        // Iterate through the array from the last index to the first
        // We are checking if we can jump to or beyond the goal from each position
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            // If the current position + the jump length from that position (nums[i])
            // is greater than or equal to the current goal, update the goal to this position
            if nums[i] + i >= goal {
                goal = i
            }
        }

        // If we've moved the goal all the way to the first index (0),
        // it means we can jump to the end of the list from the start
        return goal == 0
    }
}