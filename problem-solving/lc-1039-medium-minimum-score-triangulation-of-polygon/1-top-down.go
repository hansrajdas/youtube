/*
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Complexity
----------
Time: O(N^3)
Space: O(N^2)

Reference: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/294265/python-in-depth-explanation-dp-for-beginners/
*/

import (
    "fmt"
    "math"
)

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func minScoreTriangulation(values []int) int {
    var F func(int, int) int
    cache := make(map[string]int)

    F = func(left, right int) int {
        if right - left < 2 {
            return 0
        }
        key := fmt.Sprintf("%d-%d", left, right)
        if v, ok := cache[key]; ok {
            return v
        }
        cache[key] = math.MaxInt32
        for mid := left + 1; mid < right; mid++ {
            cache[key] = min(
                cache[key],
                values[left]*values[mid]*values[right] + F(left, mid) + F(mid, right))
        }
        return cache[key]
    }
    return F(0, len(values) - 1)
}
