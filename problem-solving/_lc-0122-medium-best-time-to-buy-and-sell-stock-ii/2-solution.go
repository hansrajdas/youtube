/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Complexity
----------
Time: O(n)
Space: O(1)

NOTE
----
Instead of finding peaks and valleys (as in ./1-solution.go) we can just add
increments (if we see a new price) and it will eventually the profit that can be earned.
*/

func maxProfit(prices []int) int {
    profit, min := 0, prices[0]
    for i := 1; i < len(prices); i++ {
        if prices[i] > min {
            profit += prices[i] - min
        }
        min = prices[i]
    }
    return profit
}
