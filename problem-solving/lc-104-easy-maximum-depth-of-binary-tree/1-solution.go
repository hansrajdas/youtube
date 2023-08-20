/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Complexity
----------
Time: O(n)
Space: O(n)
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    return 1 + max(
        maxDepth(root.Left),
        maxDepth(root.Right))
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
