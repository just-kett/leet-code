class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up = 1
        dow = 1
        max_len = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up += 1
                dow = 1      
            elif nums[i] < nums[i-1]:
                dow += 1
                up = 1
            else:
                dow = up = 1
            max_len =max(up,dow,max_len)
        return max_len