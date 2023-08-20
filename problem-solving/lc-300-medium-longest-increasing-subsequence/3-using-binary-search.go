/*
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(nlogn)
Space: O(n)

Explained here: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
*/

func binarySearch(nums []int, x int) int {
    l, r := 0, len(nums) - 1
    for l <= r {
        m := (l + r) / 2
        if nums[m] < x {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return l
}

func lengthOfLIS(nums []int) int {
    var sub []int
    for _, v := range nums {
        if len(sub) == 0 || sub[len(sub) - 1] < v {
            sub = append(sub, v)
        } else {
            idx := binarySearch(sub, v)
            sub[idx] = v
        }
    }
    return len(sub)
}
