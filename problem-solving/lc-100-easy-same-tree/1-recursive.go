/*
https://leetcode.com/problems/same-tree/

Complexity
----------
Time and Space: O(N)

Note
----
Iterative approach is not very readable for this question,
recursive is preferrable due to clean and short code.
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil || q == nil {
        return p == q
    }
    if p.Val != q.Val {
        return false
    }
    return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
