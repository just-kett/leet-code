class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def helper(a: int, b: int, s: str):
            if a==0 and b==0:
                ans.append(s)
                return
            if b>0:
                if(a>0):
                    helper(a-1,b,s+"(")
                if(b>a):
                    helper(a,b-1, s + ")")
        helper(n,n,"")
        return ans