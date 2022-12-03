"""
https://leetcode.com/problems/target-sum/

Complexity
----------
Leave as an exercise.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        This is BFS approach where we start from first level then calculate
        next level and so on using dictionary.
        https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood/934507
        """
        stage = defaultdict(int)
        stage[0] = 1
        for n in nums:
            newStage = defaultdict(int)
            for t in stage:
                newStage[t + n] += stage[t]
                newStage[t - n] += stage[t]
            stage = newStage
        return stage[target]
