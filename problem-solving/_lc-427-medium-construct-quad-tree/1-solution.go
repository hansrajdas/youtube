/*
https://leetcode.com/problems/construct-quad-tree/

Complexity
----------
Time: O(n^2)
Space: O(logn)  // We are dividing by n by half in every call.

Reference: https://leetcode.com/problems/construct-quad-tree/solutions/154565/java-recursive-solution/
*/

/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
    var F func(int, int, int) *Node
    // (r, c) is coordinates of top left.
    F = func(r, c, n int) *Node {
        if n == 1 {
            return &Node{
                Val: grid[r][c] != 0,
                IsLeaf: true,
                TopLeft: nil,
                TopRight: nil,
                BottomLeft: nil,
                BottomRight: nil,
            }
        }
        node := &Node{}
        h := n / 2
        tLeft := F(r, c, h)
        tRight := F(r, c + h, h)
        bLeft := F(r + h, c, h)
        bRight := F(r + h, c + h, h)
        // All are leaf and have same val
        if tLeft.IsLeaf && tRight.IsLeaf && bLeft.IsLeaf && bRight.IsLeaf && tLeft.Val == tRight.Val && tRight.Val == bLeft.Val && bLeft.Val == bRight.Val {
            node.Val = tLeft.Val
            node.IsLeaf = true
        } else {
            node.TopLeft = tLeft
            node.TopRight = tRight
            node.BottomLeft = bLeft
            node.BottomRight = bRight
            // node.Val can be true or false
            // node.IsLeaf will be false by default
        }
        return node
    }
    return F(0, 0, len(grid))
}
