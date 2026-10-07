class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])
        return dp[0] > 0