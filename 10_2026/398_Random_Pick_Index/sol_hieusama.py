import random
class Solution:

    def __init__(self, nums: list[int]):
        self.so_tay_vi_tri = defaultdict(list)
        for index, value in enumerate(nums):
            self.so_tay_vi_tri[value].append(index)

    def pick(self, target: int) -> int:
        danh_sach_vi_tri = self.so_tay_vi_tri[target]
        return random.choice(danh_sach_vi_tri)