class Solution:
    def rob(self, nums: list[int]) -> int:
        le = 0
        chan = 0 
        for tien in nums:
            tong = max(chan,le + tien)
            le = chan 
            chan = tong
        return tong