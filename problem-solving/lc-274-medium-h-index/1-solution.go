/*
https://leetcode.com/problems/h-index/

Complexity
----------
Time: O(n)
Space: O(n)
*/

func hIndex(citations []int) int {
    n := len(citations)
    buckets := make([]int, n + 1)
    for _, c := range citations {
        if c >= n {
            buckets[n] += 1
        } else {
            buckets[c] += 1
        }
    }

    total := 0
    for i := n; i >= 0; i-- {
        total += buckets[i]
        if total >= i {
            return i
        }
    }
    return 0
}
