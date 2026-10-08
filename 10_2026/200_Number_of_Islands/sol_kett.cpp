#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    void bfs(vector<vector<char>>& grid, int x, int y) {
        queue<pair<int, int>> q;
        q.push({x, y});
        grid[x][y] = '0';
        vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        while (!q.empty()) {
            auto xy = q.front();
            q.pop();
            int col = xy.first;
            int row = xy.second;
            for (auto i : dir) {
                int nx = col + i.first;
                int ny = row + i.second;
                if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid[0].size() && grid[nx][ny] == '1') {
                    q.push({nx, ny});
                    grid[nx][ny] = '0';
                }
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    count += 1;
                    bfs(grid, i, j);
                }
            }
        }
        return count;
    }
};