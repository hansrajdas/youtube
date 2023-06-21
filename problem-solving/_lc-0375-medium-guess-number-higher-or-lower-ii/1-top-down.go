/*
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

Complexity
----------
Time: O(n^3)
Space: O(n^2)
*/

func getMoneyAmount(n int) int {
    cache := make(map[string]int)
    var F func(int, int) int
    var temp int
    F = func(low, high int) int {
        if low >= high {
            return 0
        }
        key := fmt.Sprintf("%d-%d", low, high)
        if v, ok := cache[key]; ok {
            return v
        }
        cache[key] = math.MaxInt32
        for g := low; g <= high; g++ {
            temp = g + max(F(low, g - 1), F(g + 1, high))
            cache[key] = min(cache[key], temp)
        }
        return cache[key]
    }
    return F(1, n)
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
