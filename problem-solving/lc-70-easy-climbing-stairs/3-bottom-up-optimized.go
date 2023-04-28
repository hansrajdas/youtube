/**
 * https://leetcode.com/problems/climbing-stairs/
 * 
 * Complexity
 * ----------
 * Time: O(N)
 * Space: O(1)
 */

func climbStairs(n int) int {
    if n < 4 {
        return n
    }
    var count int
    oneAway := 3
    twoAway := 2
    for i := 4; i <= n; i++ {
        count = oneAway + twoAway
        twoAway = oneAway
        oneAway = count
    }
    return count
}
