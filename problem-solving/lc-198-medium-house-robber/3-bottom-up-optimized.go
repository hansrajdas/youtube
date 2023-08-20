/*
https://leetcode.com/problems/house-robber/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func rob(nums []int) int {
    m := len(nums)
    if m < 2 {
        return nums[0]  // Have atleast one element
    }
    twoAway := nums[0]
    oneAway := max(nums[0], nums[1])
    for i := 2; i < m; i++ {
        temp := max(
            nums[i] + twoAway,
            oneAway)
        twoAway = oneAway
        oneAway = temp
    }
    return oneAway
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
