/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Complexity
----------
Time: O(k*n)
Space: O(k*n)

Reference
---------
../_lc-0123-hard-best-time-to-buy-and-sell-stock-iii/1-top-down.py
*/

func maxProfit(k int, prices []int) int {
    cache := make(map[string]int)
    var F func(int, int, int) int
    // This function returns max profit earned.
    F = func(i, isBuy, x int) int {
        if i == len(prices) || x == k {
            return 0
        }
        key := fmt.Sprintf("%d-%d-%d", i, isBuy, x)
        if v, ok := cache[key]; ok {
            return v
        }
        if isBuy == 1 {
            cache[key] = max(
                F(i + 1, 1, x),  // Don't buy
                F(i + 1, 0, x) - prices[i])  // Buy
        } else {
            cache[key] = max(
                F(i + 1, 0, x),  // Don't sell
                F(i + 1, 1, x + 1) + prices[i])  // Sell
        }
        return cache[key]
    }
    return F(0, 1, 0)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
