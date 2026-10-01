class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        res = 0
        curr = s.count('1')
        t = '1'+s+'1'
        sec = t.split("1")
        i = 0
        while i < len(sec):
            if len(sec[i])>0:
                j = i+1
                while j< len(sec) and len(sec[j]) == 0:
                    j+=1
                if j < len(sec) and len(sec[j])>0:
                    lenght = len(sec[i])+len(sec[j])
                    res = max(res, lenght)
                i=j
            else:
                i+=1
        return res + curr    
        #print(sec)
        