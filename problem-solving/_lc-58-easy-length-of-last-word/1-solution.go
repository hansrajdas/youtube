/**
 * https://leetcode.com/problems/length-of-last-word/
 * 
 * Complexity
 * ----------
 * Time: O(n)
 * Space: O(1)
 * 
 * n = length of whole string
 */

func lengthOfLastWord(s string) int {
    count := 0
    for i := len(s) - 1; i >= 0; i-- {
        if s[i] != ' ' {
            count += 1
        } else if count > 0 {
            return count
        }
    }
    return count
}
