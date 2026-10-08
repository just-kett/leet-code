class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        cnt=0
        for x in s:
            if x== '(':
                st.append(x)
            else:
                if not st:
                    cnt+=1
                else:
                    st.pop()
        return cnt+len(st)