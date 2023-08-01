/*
https://leetcode.com/problems/house-robber/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func rob(nums []int) int {
    m := len(nums)
    if m < 2 {
        return nums[0]  // Have atleast one element
    }
    dp := make([]int, m)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i := 2; i < m; i++ {
        dp[i] = max(
            nums[i] + dp[i - 2],
            dp[i - 1])
    }
    return dp[m - 1]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
