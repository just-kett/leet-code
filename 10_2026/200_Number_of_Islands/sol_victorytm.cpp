#include <vector>
#include <stack>
#include <utility>
using namespace std;


class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m  = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m,vector<bool>(n,0));
        int cnt = 0;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(visited[i][j] || grid[i][j] == '0') continue;
                stack<pair<int,int>> st;
                st.push({i,j});
                while(!st.empty()){
                    auto a = st.top();
                    int u = a.first, v = a.second;
                    st.pop();
                    if(u>=m || u < 0 || v >= n || v < 0) continue;
                    if(visited[u][v] || grid[u][v] == '0') continue;
                    visited[u][v] = 1;
                    st.push({u+1,v});
                    st.push({u,v+1});
                    st.push({u-1,v});
                    st.push({u,v-1});
                }
                cnt++;
            }
        }
        return cnt;
    }
};