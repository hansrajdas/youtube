/*
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func longestPalindrome(words []string) int {
    ans := 0
    seen := make(map[string]int)
    for _, w := range words {
        wr := fmt.Sprintf("%c%c", w[1], w[0])
        if c, ok := seen[wr]; ok && c > 0 {
            ans += 4
            seen[wr] -= 1
        } else {
            seen[w] += 1
        }
    }
    for w, c := range seen {
        if c > 0 && w[0] == w[1] {
            return ans + 2
        }
    }
    return ans
}
