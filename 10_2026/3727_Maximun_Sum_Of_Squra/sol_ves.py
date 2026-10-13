class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x))
        n = len(nums)
        m = n//2
        return sum(x*x for x in nums[m:]) - sum(x*x for x in nums[:m])