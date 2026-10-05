class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        st = []
        for i in range (len(nums)):
            l=0
            r=len(st)
            while l<r:
                mid = (l+r)//2
                if st[mid] < nums[i]:
                    l = mid+1
                else:
                   r = mid
            if l == len(st) :
                st.append(nums[i])
            else:
                st[l] = nums[i]
        return len(st)