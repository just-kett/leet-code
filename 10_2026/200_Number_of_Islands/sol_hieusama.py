class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        so_luong_dao = 0
        da_tham = set() 

        huong_di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0" or (r, c) in da_tham:
                    continue
                so_luong_dao += 1
                da_tham.add((r, c))

                danh_sach_cho = [(r, c)]

                while danh_sach_cho:
                    curr_r, curr_c = danh_sach_cho.pop(0)
                    for dr, dc in huong_di:
                        new_r = curr_r + dr
                        new_c = curr_c + dc
                        if (
                            0 <= new_r < m
                            and 0 <= new_c < n
                            and grid[new_r][new_c] == "1"
                            and (new_r, new_c) not in da_tham):
                            da_tham.add((new_r, new_c))
                            danh_sach_cho.append((new_r, new_c)) 

        return so_luong_dao