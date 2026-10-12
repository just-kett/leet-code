class Solution:
    def __init__(self, nums: list[int]):
        self.hashmap = defaultdict(list)
        for i, x in enumerate(nums):
            self.hashmap[x].append(i)
    def pick(self, target: int) -> int:
        res = self.hashmap[target]
        return res[random.randint(0, len(res) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)