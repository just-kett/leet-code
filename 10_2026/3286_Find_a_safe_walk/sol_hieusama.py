from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        start_hp = health - grid[0][0]
        if start_hp <= 0:
            return False
        max_hp = [[-1] * n for _ in range(m)]
        max_hp[0][0] = start_hp
        q = deque([(0, 0, start_hp)])

        while q:
            r, c, hp = q.popleft()
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    next_hp = hp - grid[nr][nc]
                    if next_hp > 0 and next_hp > max_hp[nr][nc]:
                        max_hp[nr][nc] = next_hp
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc, next_hp))
                        else:
                            q.append((nr, nc, next_hp))

        return False