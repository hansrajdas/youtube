/*
https://leetcode.com/problems/unique-binary-search-trees/

Complexity
----------
Time: O(n^2)
Space: O(n)

Reference: https://leetcode.com/problems/unique-binary-search-trees/solutions/1565543/c-python-5-easy-solutions-w-explanation-optimization-from-brute-force-to-dp-to-catalan-o-n/
*/

func numTrees(n int) int {
    dp := make([]int, n + 1)
    dp[0], dp[1] = 1, 1

    for i := 2; i <= n; i++ {
        for j := 1; j <= i; j++ {
            dp[i] += dp[j - 1] * dp[i - j]
        }
    }
    return dp[n]
}
