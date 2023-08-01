/*
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Complexity
----------
Time: O(m*n)
Space: O(m*n)

NOTE
----
This can be solved in linear time using standard pattern matching algorithms like
KMP, Rabin karp, ...
*/

func strStr(haystack string, needle string) int {
    var i, j int
    for i = 0; i < len(haystack) - len(needle) + 1; i++ {
        for j = 0; j < len(needle); j++ {
            if haystack[i + j] != needle[j] {
                break
            }
        }
        if j == len(needle) {
            return i
        }
    }
    return -1
}
