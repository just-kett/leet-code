class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        visited = {}
        def dfs(s1, s2):
            if (s1, s2) in visited:
                return visited[(s1,s2)]
            if s1 == s2:
                visited [(s1,s2)] = True
                return True
            if sorted(s1) != sorted(s2):
                visited [(s1,s2)] = False
                return False
            n = len(s1)
            for i in range (1,n):
                if dfs(s1[i:], s2[i:]) and dfs(s1[:i], s2[:i]):
                    visited[(s1,s2)] = True
                    return True
                if dfs(s1[i:], s2[:-i]) and dfs(s1[:i], s2[-i:]):
                    visited[(s1,s2)] = True
                    return True
            
            visited[(s1,s2)] = False
            return False
        return dfs(s1,s2)
