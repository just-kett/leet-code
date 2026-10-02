import math

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        khoang_cach = []
        index = 0
        for i in points:
            x = i[0]**2 + i[1]**2
            khoang_cach.append([index, x])
            index += 1
        result = []
        khoang_cach.sort(key=lambda item: item[1])
        for i in range(k):
            result.append(points[khoang_cach[i][0]])
        return result
