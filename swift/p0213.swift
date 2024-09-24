class Solution {
    func rob(_ nums: [Int]) -> Int {

        // Edge cases
        if nums.count == 1 {
            return nums[0]
        }

        if nums.count == 2 {
            return max(nums[0], nums[1])
        }

        // Robbing First House (from index 0 to nums.count - 2)
        var previous_house = 0
        var two_houses_ago = 0
        var current_max = 0

        for i in 0..<nums.count-1 {
            current_max = max(previous_house, two_houses_ago + nums[i])
            two_houses_ago = previous_house
            previous_house = current_max
        }

        let robbing_first_house_max = previous_house

        // Robbing Second House (from index 1 to nums.count - 1)
        previous_house = 0
        two_houses_ago = 0
        current_max = 0

        for i in 1..<nums.count {
            current_max = max(previous_house, two_houses_ago + nums[i])
            two_houses_ago = previous_house
            previous_house = current_max
        }

        let robbing_second_house_max = previous_house

        // Return the maximum of robbing the first house or the second house
        return max(robbing_first_house_max, robbing_second_house_max)
    }
}
