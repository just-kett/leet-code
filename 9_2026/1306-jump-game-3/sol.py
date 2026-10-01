from collections import deque
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        visited = set([start])
        
        #bfs
        while q:
            curr = q.popleft()
            #check
            if arr[curr] == 0:
                return True
            
            jump1 = curr - arr[curr]
            jump2 = curr + arr[curr]
            #check
            if jump1 >= 0 and jump1 < n:
                if jump1 not in visited:
                    visited.add(jump1)
                    q.append(jump1)            
            if jump2 >= 0 and jump2 < n:
                if jump2 not in visited:
                    visited.add(jump2)
                    q.append(jump2)
        return False   
            