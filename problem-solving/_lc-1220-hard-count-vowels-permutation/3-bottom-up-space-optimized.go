/*
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time: O(n)
Space: O(1)
*/

func countVowelPermutation(n int) int {
    M := 1000000007
    a, e, i, o, u := 1, 1, 1, 1, 1
    for idx := 1; idx < n; idx++ {
        // Previous counts
        pa, pe, pi, po, pu := a, e, i, o, u

        // a can be after e, i or u, and so on...
        a = (pe + pi + pu) % M
        e = (pa + pi) % M
        i = (pe + po) % M
        o = pi
        u = (pi + po) % M
    }
    return (a + e + i + o + u) % M
}
