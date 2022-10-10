"""
https://leetcode.com/problems/dungeon-game/

Complexity
----------
Time: O(mn)
Space: O(mn)
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        cache = {}
        def minHP(r, c):
            if r == rows or c == cols:
                return math.inf
            if r == rows - 1 and c == cols - 1:
                return -dungeon[r][c] + 1 if dungeon[r][c] <= 0 else 1
            if (r, c) in cache:
                return cache[(r, c)]
            right = minHP(r, c + 1)
            down = minHP(r + 1, c)
            minRequired = min(right, down) - dungeon[r][c]

            # Below condition seems to be oposite but correct, see the above
            # line, if current cell has high positive value then
            # `minRequired` will be highly negative so that's the reason,
            # we are keeping 1 if minRequired is less than 0 else that
            # positive value
            cache[(r, c)] = 1 if minRequired <= 0 else minRequired
            return cache[(r, c)]
        return minHP(0, 0)
