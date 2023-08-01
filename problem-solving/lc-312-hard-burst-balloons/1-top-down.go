/*
https://leetcode.com/problems/burst-balloons/

Complexity
----------
Time: O(n^3)
Space: O(n^2)

Reference
---------
Explanation: https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
Code: https://leetcode.com/problems/burst-balloons/solutions/76228/share-some-analysis-and-explanations/

NOTE: This gives TLE in golang although got submitted in python but slow.
*/

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func maxCoins(nums []int) int {
    N := make([]int, len(nums) + 2)
    copy(N[1:], nums)
    N[0], N[len(N) - 1] = 1, 1
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(l, r int) int {
        if l > r {
            return 0
        }
        key := fmt.Sprintf("%d-%d", l, r)
        if v, ok := cache[key]; ok {
            return v
        }
        for m := l + 1; m < r; m++ {
            cache[key] = max(
                cache[key],
                N[l]*N[m]*N[r] + F(l, m) + F(m, r))
        }
        return cache[key]
    }
    return F(0, len(N) - 1)
}
