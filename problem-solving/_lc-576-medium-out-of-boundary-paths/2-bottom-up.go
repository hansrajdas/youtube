/*
https://leetcode.com/problems/out-of-boundary-paths

Complexity
----------
Time: O(mnN)
Space: O(mn)

N = maxMove

Reference: https://leetcode.com/problems/out-of-boundary-paths/editorial/ [Approach 3]
*/

func getMatrix(rows, cols int) [][]int {
    var m [][]int
    for i := 0; i < rows; i++ {
        m = append(m, make([]int, cols))
    }
    return m
}

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
    count, M := 0, 1000000007
    dp := getMatrix(m, n)
    dp[startRow][startColumn] = 1
    for i := 0; i < maxMove; i++ {
        // If we alter the dp array, now some of the entries will correspond to x−1 moves and the updated ones will correspond to x moves so taking temp.
        temp := getMatrix(m, n)
        for r := 0; r < m; r++ {
            for c := 0; c < n; c++ {
                // If on boundary then in next move we can go out of boundary so sum all numbers to reach boundary till previous move.
                if r == 0 {
                    count = (count + dp[r][c]) % M
                }
                if r == m - 1 {
                    count = (count + dp[r][c]) % M
                }
                if c == 0 {
                    count = (count + dp[r][c]) % M
                }
                if c == n - 1 {
                    count = (count + dp[r][c]) % M
                }

                // Update temp and retain dp.
                if r > 0 {
                    temp[r][c] = dp[r - 1][c] % M
                }
                if r < m - 1 {
                    temp[r][c] = (temp[r][c] + dp[r + 1][c]) % M
                }
                if c > 0 {
                    temp[r][c] = (temp[r][c] + dp[r][c - 1]) % M
                }
                if c < n - 1 {
                    temp[r][c] = (temp[r][c] + dp[r][c + 1]) % M
                }
            }
        }
        dp = temp
    }
    return count
}
