/*
https://leetcode.com/problems/longest-palindromic-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n^2)
*/

func longestPalindromeSubseq(s string) int {
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(l, r int) int {
        if l > r {
            return 0
        }
        if l == r {
            return 1
        }
        key := fmt.Sprintf("%d-%d", l, r)
        if v, ok := cache[key]; ok {
            return v
        }
        if s[l] == s[r] {
            cache[key] = 2 + F(l + 1, r - 1)
        } else {
            cache[key] = max(F(l + 1, r), F(l, r - 1))
        }
        return cache[key]
    }
    return F(0, len(s) - 1)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
