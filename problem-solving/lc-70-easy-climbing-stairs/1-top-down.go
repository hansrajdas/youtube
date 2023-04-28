/**
 * https://leetcode.com/problems/climbing-stairs/
 * 
 * Complexity
 * ----------
 * Time: O(N)
 * Space: O(N)
 */

var mem = make(map[int]int)

func climbStairs(n int) int {
    if n < 4 {
        return n
    }
    if v, ok := mem[n]; ok {
        return v
    }
    mem[n] = climbStairs(n - 1) + climbStairs(n - 2)
    return mem[n]
}
