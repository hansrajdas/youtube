/*
https://leetcode.com/problems/binary-tree-level-order-traversal/

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
func levelOrder(root *TreeNode) [][]int {
    var levels [][]int
    if root == nil {
        return levels
    }
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        var level []int
        count := len(queue)
        for i := 0; i < count; i++ {
            node := queue[0]
            queue = queue[1:]
            level = append(level, node.Val)
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        levels = append(levels, level)
    }
    return levels
}
