/*
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n)
*/

func lengthOfLIS(nums []int) int {
    var dp []int
    n := len(nums)
    for i := 0; i < n; i++ {
        dp = append(dp, 1)
    }

    for i := 0; i < n; i++ {
        for j := 0; j < i; j++ {
            if nums[j] < nums[i] && dp[i] < dp[j] + 1 {
                dp[i] = dp[j] + 1
            }
        }
    }

    res := dp[0]
    for _, v := range dp {
        if res < v {
            res = v
        }
    }
    return res
}
