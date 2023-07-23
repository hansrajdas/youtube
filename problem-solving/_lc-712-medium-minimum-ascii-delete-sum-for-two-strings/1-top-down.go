/*
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Complexity
----------
Time: O(m*n)
Space: O(m*n)
*/

func minimumDeleteSum(s1 string, s2 string) int {
    m, n := len(s1), len(s2)
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(i, j int) int {
        if i == m && j == n {
            return 0
        }
        if i == m {
            return ascii(s2, j)
        }
        if j == n {
            return ascii(s1, i)
        }
        key := fmt.Sprintf("%d-%d", i, j)
        if v, ok := cache[key]; ok {
            return v
        }
        if s1[i] == s2[j] {
            cache[key] = F(i + 1, j + 1)
        } else {
            cache[key] = min(
                int(s1[i]) + F(i + 1, j),
                int(s2[j]) + F(i, j + 1))
        }
        return cache[key]
    }
    return F(0, 0)
}

func ascii(s string, startIdx int) int {
    var v int
    for i := startIdx; i < len(s); i++ {
        v += int(s[i])
    }
    return v
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
