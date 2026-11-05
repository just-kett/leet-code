class Solution:
    def minMoves(self, nums: List[int]) -> int:
        chot = max(nums)
        n = len(nums)
        res = 0
        for i in range(0,n):
            bien = chot - nums[i]
            res += bien
        
        return res