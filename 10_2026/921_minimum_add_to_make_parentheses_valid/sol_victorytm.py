class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        l = []
        for c in s:
            if(c == '('):
                l.append(c)
            else:
                if l:
                    l.pop(0)
                else:
                    ans += 1
        return ans + len(l)
