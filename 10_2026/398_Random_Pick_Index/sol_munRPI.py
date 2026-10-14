class Solution:
    def __init__(self, nums: list[int]):
        self.d = {}
        for i, x in enumerate(nums):
            self.d.setdefault(x, []).append(i)
    def pick(self, target: int) -> int:
        return random.choice(self.d[target])