/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Complexity
----------
Time: O(n)
Space: O(n)

Reference
---------
Approach-3: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/796990/c-worst-to-best-solution-explained-for-dummies-like-me/
*/

func maxProfit(prices []int) int {
    buy1, buy2 := math.MaxInt32, math.MaxInt32
    profit1, profit2 := math.MinInt32, math.MinInt32
    for i := 0; i < len(prices); i++ {
        buy1 = min(buy1, prices[i])
        profit1 = max(profit1, prices[i] - buy1)
        buy2 = min(buy2, prices[i] - profit1)
        profit2 = max(profit2, prices[i] - buy2)
    }
    return profit2
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
