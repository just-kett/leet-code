# Dell biet dp, dell biet toi uu
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # define dp[i][j]: first i elements, only j elements is selected to the positive sides
        n = len(nums)
        nums = [abs(i) for i in nums]
        nums = sorted(nums)
        res = 0
        cnt = n//2
        for a in nums:
            if(cnt == 0):
                res+=a*a
                continue
            res -= a*a
            cnt-=1
        return res


