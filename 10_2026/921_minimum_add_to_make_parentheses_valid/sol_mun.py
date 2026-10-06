class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mo = 0
        them = 0
        for i in s:
            if i == '(':
                mo += 1
            elif i == ')':
                if mo > 0:
                    mo -= 1
                else:
                    them += 1
        return mo + them