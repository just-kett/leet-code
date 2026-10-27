import bisect
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        kq = [i for i in range(bisect.bisect_left(nums,target),bisect.bisect_right(nums,target))]
        return kq
