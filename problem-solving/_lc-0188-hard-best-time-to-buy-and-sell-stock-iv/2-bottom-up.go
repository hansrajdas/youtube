/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Complexity
----------
Time: O(k*n)
Space: O(k)

Reference
---------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/solutions/54125/very-understandable-solution-by-reusing-problem-iii-idea/comments/1243324
*/

func maxProfit(k int, prices []int) int {
    var buy []int
    profit := make([]int, k + 1)
    for idx := 0; idx <= k; idx++ {
        buy = append(buy, math.MaxInt32)
    }
    for p := 0; p < len(prices); p++ {
        for i := 1; i <= k; i++ {
            buy[i] = min(buy[i], prices[p] - profit[i - 1])
            profit[i] = max(profit[i], prices[p] - buy[i])
        }
    }
    return profit[k]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
