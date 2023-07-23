/*
https://leetcode.com/problems/edit-distance/

Complexity
----------
Time: O(m*n)
Space: O(m*n)

m and n are lengths of 2 strings.
*/

func minDistance(word1 string, word2 string) int {
    cache := make(map[string]int)
    var F func(int, int) int
    F = func(i, j int) int {
        if i == len(word1) {
            return len(word2) - j
        }
        if j == len(word2) {
            return len(word1) - i
        }
        key := fmt.Sprintf("%d-%d", i, j)
        if v, ok := cache[key]; ok {
            return v
        }
        if word1[i] == word2[j] {
            cache[key] = F(i + 1, j + 1)
        } else {
            cache[key] = 1 + min(
                F(i + 1, j),      // Delete
                F(i, j + 1),      // Insert
                F(i + 1, j + 1),  // Replace
            )
        }
        return cache[key]
    }
    return F(0, 0)
}

func min(x, y, z int) int {
    if x < y && x < z {
        return x
    } else if y < x && y < z {
        return y
    }
    return z
}
