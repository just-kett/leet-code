class Solution:
    def __init__(self):
        self.res = []
    def backtrack (self, s, open, close, n):
        if len(s) == n*2:
            self.res.append(s)
            return
        if open < n:
            self.backtrack(s+'(', open+1, close, n)
        if close < open:
            self.backtrack(s+')', open, close+1, n)
    def generateParenthesis(self, n: int) -> list[str]:
        self.res
        self.backtrack("", 0, 0, n)
        return self.res
        