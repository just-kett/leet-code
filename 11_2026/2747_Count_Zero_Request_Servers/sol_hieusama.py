class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        dic = {}
        for truy in logs:
            key = str(truy[0])
            if key not in dic:
                dic[key] = []
            dic[key].append(truy[1])
        giai = []
        for time in queries:
            start = time - x
            end = time
            res = [] 
            for key, lit in dic.items():
                for tm in lit:
                    if start <= tm <= end:
                        res.append(int(key))
                        break
            giai.append(n - len(res))
        return giai