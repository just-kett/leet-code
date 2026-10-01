import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        
        for p in points:
            length = p[0]**2 + p[1]**2
            heapq.heappush(pq, (-length, p))
            if len(pq) > k:
                heapq.heappop(pq)
                
        return [p for length, p in pq]