/*
https://leetcode.com/problems/remove-element/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func removeElement(nums []int, val int) int {
    var i int
    for _, x := range nums {
        if x != val {
            nums[i] = x
            i += 1
        }
    }
    return i
}
