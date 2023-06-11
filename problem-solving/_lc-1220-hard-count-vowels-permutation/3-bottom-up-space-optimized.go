/*
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time: O(5*n) => O(n)
Space: O(1)
*/

func countVowelPermutation(n int) int {
    M := 1000000007
    a, e, i, o, u := 1, 1, 1, 1, 1
    for idx := 1; idx < n; idx++ {
        // Previous counts
        pa, pe, pi, po, pu := a, e, i, o, u
        for _, c := range []rune{'a', 'e', 'i', 'o', 'u'} {
            // After which chars, we can have current char
            if c == 'a' {
                a = (pe + pi + pu) % M
            } else if c == 'e' {
                e = (pa + pi) % M
            } else if c == 'i' {
                i = (pe + po) % M
            } else if c == 'o' {
                o = pi % M
            } else {
                u = (pi + po) % M
            }
        }
    }
    return (a + e + i + o + u) % M
}
