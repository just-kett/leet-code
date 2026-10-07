# AE nào không hiểu sol thì đọc đây:
# https://cp-algorithms.com/game_theory/sprague-grundy-nim.html

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        sum = 0
        for i in piles:
            sum ^= i
        return sum != 0