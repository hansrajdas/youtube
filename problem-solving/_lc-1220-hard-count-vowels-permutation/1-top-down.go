/*
https://leetcode.com/problems/count-vowels-permutation/

Complexity
----------
Time and space: O(5*n) => O(n)
*/

func countVowelPermutation(n int) int {
    M := 1000000007
    cache := make(map[string]int)
    // '*' is used to handle initial condition, when we don't
    // previous char and can have any of 5 vowels.
    nextChars := map[rune][]rune{
        '*': {'a', 'e', 'i', 'o', 'u'},
        'a': {'e'},
        'e': {'a', 'i'},
        'i': {'a', 'e', 'o', 'u'},
        'o': {'i', 'u'},
        'u': {'a'},
    }
    var F func(rune, int) int
    F = func(lastChar rune, vowelCount int) int {
        if vowelCount == n {
            return 1
        }
        key := fmt.Sprintf("%c-%d", lastChar, vowelCount)
        if v, ok := cache[key]; ok {
            return v
        }
        for _, v := range nextChars[lastChar] {
            cache[key] = (cache[key] + F(v, vowelCount + 1)) % M
        }
        return cache[key]
    }
    return F('*', 0)
}
