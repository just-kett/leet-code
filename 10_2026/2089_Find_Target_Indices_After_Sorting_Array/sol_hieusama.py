class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        lis = []
        n = len(nums)  
        for i in range(n):
            if nums[i] == target:
                lis.append(i)

        if len(lis) == 0:
            return []
        return lis