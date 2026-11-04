class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0,0] for i in range(n)]
        dp[0][1] = nums[0]
        #dp i j: index i has flag j (taken = 1)
        for i in range(1,n):
            dp[i][0] = max(dp[i][0], max(dp[i-1][1],dp[i-1][0]))
            dp[i][1] = max(dp[i][1], dp[i-1][0] + nums[i])
        return max(dp[n-1][0], dp[n-1][1])