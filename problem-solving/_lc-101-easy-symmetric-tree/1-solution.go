/*
https://leetcode.com/problems/symmetric-tree/

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
func isSymmetric(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return checkSymmetric(root.Left, root.Right)
}

func checkSymmetric(left, right *TreeNode) bool {
    if left == nil || right == nil {
        return left == right
    }
    if left.Val != right.Val {
        return false
    }
    return checkSymmetric(left.Left, right.Right) && checkSymmetric(left.Right, right.Left)
}
