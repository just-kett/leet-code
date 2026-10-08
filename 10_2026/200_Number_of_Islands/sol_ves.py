class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        cnt = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    cnt+=1
                    grid[r][c]="0"
                    queue = deque([(r,c)])
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for dr,dc in dirs:
                            nr = curr_r + dr
                            nc = curr_c + dc
                            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1":
                                grid[nr][nc] ="0"
                                queue.append((nr,nc))
        return cnt
