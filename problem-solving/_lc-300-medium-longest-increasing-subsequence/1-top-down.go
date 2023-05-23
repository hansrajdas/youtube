/*
https://leetcode.com/problems/longest-increasing-subsequence/

Complexity
----------
Time: O(n^2)
Space: O(n^2)

NOTE: This solution is not accepted, gives "Time limit exceeded"
*/

func lengthOfLIS(nums []int) int {
    cache := make(map[string]int)
    var F func(int, int) int
    F = func (prev, idx int) int {
        if idx == len(nums) {
            return 0
        }
        key := fmt.Sprintf("%d-%d", prev, idx)
        if v, ok := cache[key]; ok {
            return v
        }
        notTaken := F(prev, idx + 1)
        taken := 0
        if nums[idx] > prev {
            taken = 1 + F(nums[idx], idx + 1)
        }
        if taken > notTaken {
            cache[key] = taken
        } else {
            cache[key] = notTaken
        }
        return cache[key]
    }
    return F(-math.MaxInt32, 0)
}
