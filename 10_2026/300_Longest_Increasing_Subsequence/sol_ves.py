class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res_arr = []
        for i in nums:
            left = 0
            right = len(res_arr) -1
            dummy = len(res_arr)
            while left <= right:
                mid = (right + left)//2
                if res_arr[mid] >= i:
                    dummy = mid
                    right = mid -1
                else:
                    left = mid +1
            if dummy == len(res_arr):
                res_arr.append(i)
            else:
                res_arr[dummy] = i
        return len(res_arr)

