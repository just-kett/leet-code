#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        queue<pair<int, int>> q;
        int dx[] = {1, 0 , 0, -1};
        int dy[] = {0, 1, -1, 0};
        int m = grid.size();
        int n = grid[0].size();
        q.push({0, 0});
        int starth = health - grid[0][0];
        vector<vector<int>> currenth(m, vector<int>(n, -1));
        currenth[0][0] = starth;
        if (starth <= 0) {
            return false;
        }
        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            if (x == m - 1 && y == n - 1 && currenth[x][y] >= 1) {
                return true;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    int new_h = currenth[x][y] - grid[nx][ny];
                    if (new_h >= 1 && new_h > currenth[nx][ny]) {
                        currenth[nx][ny] = new_h;
                        q.push({nx, ny});
                    }
                }
            }
        }
        return currenth[m - 1][n - 1] >= 1;
    }
};