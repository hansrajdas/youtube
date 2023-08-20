/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Complexity
----------
Time: O(n)
Space: O(1)

NOTE
----
This is a peak valley problem, we have to buy and valleys and sell at peaks.
*/


func maxProfit(prices []int) int {
    buy, profit, n := 0, 0, len(prices)
    for i := 0; i < n; i++ {
        for ;i < n - 1 && prices[i] > prices[i + 1]; i++ {}
        buy = prices[i]

        for ;i < n - 1 && prices[i] < prices[i + 1]; i++ {}
        profit += prices[i] - buy
    }
    return profit
}
