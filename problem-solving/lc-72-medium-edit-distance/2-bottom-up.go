/*
https://leetcode.com/problems/edit-distance/

Complexity
----------
Time: O(m*n)
Space: O(m*n)

m and n are lengths of 2 strings.
*/

func minDistance(word1 string, word2 string) int {
    var dp [][]int
    m, n := len(word1), len(word2)

    for i := 0; i < m + 1; i++ {
        dp = append(dp, make([]int, n + 1))
    }

    for i := 1; i < m + 1; i++ {
        dp[i][0] = i
    }
    for j := 1; j < n + 1; j++ {
        dp[0][j] = j
    }

    for i := 1; i < m + 1; i++ {
        for j := 1; j < n + 1; j++ {
            if word1[i - 1] == word2[j - 1] {
                dp[i][j] = dp[i - 1][j - 1]
            } else {
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      // Delete
                    dp[i][j - 1],      // Add
                    dp[i - 1][j - 1],  // Replace
                )
            }
        }
    }
    return dp[m][n]
}

func min(x, y, z int) int {
    if x < y && x < z {
        return x
    } else if y < x && y < z {
        return y
    }
    return z
}
