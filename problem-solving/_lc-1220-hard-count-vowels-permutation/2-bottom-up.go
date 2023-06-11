/*
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(5*n) => O(n)
*/

func countVowelPermutation(n int) int {
    M := 1000000007
    var dp [][]int
    for i := 0; i < n; i++ {
        dp = append(dp, make([]int, 5))
    }
    dp[0] = []int{1, 1, 1, 1, 1}
    for idx := 1; idx < n; idx++ {
        // Previous counts
        a, e, i, o, u := dp[idx - 1][0], dp[idx - 1][1], dp[idx - 1][2], dp[idx - 1][3], dp[idx - 1][4]
        for _, c := range []rune{'a', 'e', 'i', 'o', 'u'} {
            // After which chars, we can have current char
            if c == 'a' {
                dp[idx][0] = (e + i + u) % M
            } else if c == 'e' {
                dp[idx][1] = (a + i) % M
            } else if c == 'i' {
                dp[idx][2] = (e + o) % M
            } else if c == 'o' {
                dp[idx][3] = i % M
            } else {
                dp[idx][4] = (i + o) % M
            }
        }
    }

    var ans int
    for _, v := range dp[n - 1] {
        ans = (ans + v) % M
    }
    return ans
}
