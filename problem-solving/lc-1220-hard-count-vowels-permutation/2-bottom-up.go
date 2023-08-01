/*
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(n)
*/

func countVowelPermutation(n int) int {
    M := 1000000007
    var dp [][]int
    for i := 0; i < n; i++ {
        dp = append(dp, make([]int, 5))
    }
    dp[0] = []int{1, 1, 1, 1, 1}
    for idx := 1; idx < n; idx++ {
        // Previous counts
        a, e, i, o, u := dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][2], dp[idx - 1][3], dp[idx - 1][4]

        // a can be after e, i or u, and so on...
        dp[idx][0] = (e + i + u) % M
        dp[idx][1] = (a + i) % M
        dp[idx][2] = (e + o) % M
        dp[idx][3] = i % M
        dp[idx][4] = (i + o) % M
    }

    var ans int
    for _, v := range dp[n - 1] {
        ans = (ans + v) % M
    }
    return ans
}
