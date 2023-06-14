/*
https://leetcode.com/problems/unique-binary-search-trees/

Complexity
----------
Time: O(n^2)
Space: O(n)

Reference: https://leetcode.com/problems/unique-binary-search-trees/solutions/1565543/c-python-5-easy-solutions-w-explanation-optimization-from-brute-force-to-dp-to-catalan-o-n/
*/

var cache = map[int]int{}

func numTrees(n int) int {
    if n <= 1 {
        return 1
    }
    if v, ok := cache[n]; ok {
        return v
    }
    for i := 1; i <= n; i++ {
        cache[n] += numTrees(i - 1) * numTrees(n - i)
    }
    return cache[n]
}
