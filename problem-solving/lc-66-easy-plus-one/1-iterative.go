/**
 * https://leetcode.com/problems/plus-one/
 * 
 * Complexity
 * ----------
 * Time: O(n)
 * Space: (1)
 */

func plusOne(digits []int) []int {
    for i := len(digits) - 1; i >= 0; i-- {
        if digits[i] == 9 {
            digits[i] = 0
        } else {
            digits[i] += 1
            return digits
        }
    }
    return append([]int{1}, digits...)
}
