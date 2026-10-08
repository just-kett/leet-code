class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        hang, cot = len(grid), len(grid[0])
        islands = 0
        def dfs(h, c):
            if h < 0 or c < 0 or h >= hang or c >= cot or grid[h][c] == '0':
                return
            grid[h][c] = '0'
            dfs(h + 1, c)
            dfs(h - 1, c)
            dfs(h, c + 1)
            dfs(h, c - 1)
        for h in range(hang):
            for c in range(cot):
                if grid[h][c] == '1':
                    islands += 1
                    dfs(h, c)
        return islands