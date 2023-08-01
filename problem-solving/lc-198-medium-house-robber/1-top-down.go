/*
https://leetcode.com/problems/house-robber/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func rob(nums []int) int {
    cache := make(map[int]int)
    var robMax func(int) int
    robMax = func(i int) int {
        if i >= len(nums) {
            return 0
        }
        if v, ok := cache[i]; ok {
            return v
        }
        cache[i] = max(
            nums[i] + robMax(i + 2),
            robMax(i + 1))
        return cache[i]
    }
    return robMax(0)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
