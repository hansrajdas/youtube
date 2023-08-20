/*
https://leetcode.com/problems/distinct-subsequences/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func numDistinct(s string, t string) int {
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(i, j int) int {
        if j == len(t) {
            return 1
        }
        if i == len(s) {
            return 0
        }
        key := fmt.Sprintf("%d-%d", i, j)
        if v, ok := cache[key]; ok {
            return v
        }
        if s[i] == t[j] {
            cache[key] = F(i + 1, j) + F(i + 1, j + 1)
        } else {
            cache[key] = F(i + 1, j)
        }
        return cache[key]
    }
    return F(0, 0)
}
