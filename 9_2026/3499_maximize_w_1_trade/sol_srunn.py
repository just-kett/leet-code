class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_1 = s.count("1")
        l_0 = 0
        max_gain = 0
        i = 0
        while i < len(s) and s[i] == "1":
            i += 1
        while i < len(s):

            l_0 = 0
            while i < len(s) and s[i] == "0":
                l_0 += 1
                i += 1
            if i == len(s):
                break

            while i < len(s) and s[i] == "1":
                i += 1
            if i == len(s):
                break
            r_0 = 0
            j = i
            while j < len(s) and s[j] == "0":
                r_0 += 1
                j += 1
            max_gain = max(max_gain, l_0 + r_0)
        return total_1 + max_gain

        