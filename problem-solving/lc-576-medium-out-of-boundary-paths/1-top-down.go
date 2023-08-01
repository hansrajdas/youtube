/*
https://leetcode.com/problems/out-of-boundary-paths

Complexity
----------
Time: O(mnN)
Space: O(mnN)

N = maxMove
*/

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
    M := 1000000007
    cache := make(map[string]int)
    var P func(int, int, int) int
    P = func(r, c, movesLeft int) int {
        if r < 0 || r >= m || c < 0 || c >= n {
            return 1
        }
        if movesLeft == 0 {
            return 0
        }
        key := fmt.Sprint("%d-%d-%d", r, c, movesLeft)
        if v, ok := cache[key]; ok {
            return v
        }
        cache[key] = (
            P(r + 1, c, movesLeft - 1) +
            P(r - 1, c, movesLeft - 1) +
            P(r, c + 1, movesLeft - 1) +
            P(r, c - 1, movesLeft - 1)) % M
        return cache[key]
    }
    return P(startRow, startColumn, maxMove)
}
