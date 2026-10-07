class Solution(object):
    def stoneGame(self, piles):
        left = 0 
        right = len(piles) - 1  
        dic = {}  

        def minimax(trai: int, phai: int, luot_Alice: bool) -> int:
            if trai > phai: 
                return 0

           
            state = (trai, phai, luot_Alice)
            if state in dic:
                return dic[state]

            if luot_Alice:
                lay_trai = piles[trai] + minimax(trai + 1, phai, False)
                lay_phai = piles[phai] + minimax(trai, phai - 1, False)
                stone = max(lay_trai, lay_phai)
            else:
                lay_trai = -piles[trai] + minimax(trai + 1, phai, True)
                lay_phai = -piles[phai] + minimax(trai, phai - 1, True)
                stone = min(lay_trai, lay_phai)
            
            dic[state] = stone
            return stone

        return minimax(left, right, True) > 0