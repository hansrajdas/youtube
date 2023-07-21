/*
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Complexity
----------
Time: O(n)
Space: O(n)

Reference
---------
Approach-1: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/796990/c-worst-to-best-solution-explained-for-dummies-like-me/
*/

func maxProfit(prices []int) int {
    cache := make(map[string]int)
    var F func(int, int, int) int
    F = func(i, isBuy, k int) int {
        if i == len(prices) || k == 2 {
            return 0
        }
        key := fmt.Sprintf("%d-%d-%d", i, isBuy, k)
        if v, ok := cache[key]; ok {
            return v
        }
        if isBuy == 1 {
            cache[key] = max(
                F(i + 1, 1, k),  // Don't buy
                F(i + 1, 0, k) - prices[i])  // Buy
        } else {
            cache[key] = max(
                F(i + 1, 0, k),  // Don't sell
                F(i + 1, 1, k + 1) + prices[i])  // Sell
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
