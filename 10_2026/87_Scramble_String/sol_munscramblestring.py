class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        archive={} #lưu trữ từng tập kết quả
        def dp(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2): 
                return False
            if (s1, s2) in archive:
                return archive[(s1, s2)]
            n = len(s1)
            #slicing để lấy các phần bị chia của s1, s2, so sánh với nhau bằng hàm đệ quy dp
            for i in range(1, n):
                if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]): 
                    archive[(s1, s2)] = True
                    return True
                if dp(s1[:i], s2[n-i:]) and dp(s1[i:], s2[:n-i]):
                    archive[(s1, s2)] = True
                    return True
            archive[(s1, s2)] = False
            return False
        return dp(s1, s2)