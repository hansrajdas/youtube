/*
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps

Complexity
----------
Time: O(S*N)
Space: O(S*N)

S = Steps
N = arrLen
*/

func numWays(steps int, arrLen int) int {
    M := 1000000007
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(idx, stepsLeft int) int {
        if idx < 0 || idx == arrLen {
            return 0
        }
        if stepsLeft == 0 {
            if idx == 0 {
                return 1
            }
            return 0
        }
        key := fmt.Sprintf("%d-%d", idx, stepsLeft)
        if v, ok := cache[key]; ok {
            return v
        }
        cache[key] = (F(idx, stepsLeft - 1) +
                      F(idx - 1, stepsLeft - 1) +
                      F(idx + 1, stepsLeft - 1)) % M
        return cache[key]
    }
    return F(0, steps)
}
