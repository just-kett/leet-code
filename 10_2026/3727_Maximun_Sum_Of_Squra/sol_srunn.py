class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: abs(x), reverse=True)
        sum=0
        mid = (n+1)//2
        for i in range(n):
            if i <mid:
                sum+=nums[i]**2
            else:
                sum-=nums[i]**2
            print(sum)
        return sum
