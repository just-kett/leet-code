class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        sq = sorted([x * x for x in nums])
        n = len(sq)
        ans = sum(sq[n // 2:]) - sum(sq[:n // 2])
        return ans