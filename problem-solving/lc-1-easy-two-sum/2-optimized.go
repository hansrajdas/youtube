/*
Problem: https://leetcode.com/problems/two-sum/

Complexity
----------
Time: O(N)
Space: O(N)
*/

func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, n := range nums {
        if idx, ok := seen[target - n]; ok {
            return []int{i, idx}
        }
        seen[n] = i
    }
    return []int{}
}
