class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        right = 0
        left = len(nums) - 1 
        score = 0 
        while nums:
            vl = nums[left]
            vr = nums[right]
            if len(nums) % 2 == 0:
                if left <= right:
                    break
                score += vl*vl
                score -= vr*vr
                left = left - 1
                right = right + 1
            else:
                if left <= right:
                    score += vl*vl   
                    break
                score += vl*vl
                score -= vr*vr
                left = left - 1
                right = right + 1
        return score