/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func maxProfit(prices []int) int {
    buy, profit := prices[0], 0
    for i := 1; i < len(prices); i++ {
        if profit < prices[i] - buy {
            profit = prices[i] - buy
        }
        if prices[i] < buy {
            buy = prices[i]
        }
    }
    return profit
}
