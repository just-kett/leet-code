class Solution(object):
    def minAddToMakeValid(self, s):
        count = 0
        push = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                if count > 0:
                    count = count - 1
                else: 
                    push += 1
        return push + count