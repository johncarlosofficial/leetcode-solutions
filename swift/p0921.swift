class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var opening: Int = 0  // Counter for unmatched opening parentheses
        var closing: Int = 0  // Counter for unmatched closing parentheses

        // Iterate through each character in the input string
        for char: Character in s {
            if char == "(" {
                opening += 1  // Increment opening counter for every '('
            } else if opening > 0 {
                opening -= 1  // If there is an unmatched '(', decrement it for every ')'
            } else {
                closing += 1  // If no unmatched '(', increment closing counter for every unmatched ')'
            }
        }

        // The total moves required to make the string valid is the sum of unmatched opening 
        // and closing parentheses
        return opening + closing
    }
}
