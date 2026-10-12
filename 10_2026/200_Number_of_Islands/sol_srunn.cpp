class Solution {
public:
    vector<pair<int, int>> v = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    vector<vector<bool>>visited;
    void bfs(vector<vector<char>>& grid,int x,int y)
    {
        int m=grid.size(),n=grid[0].size();
        queue<pair<int,int>>q;
        visited[x][y]=true;
        q.push({x,y});
        while(!q.empty())
        {
            x=q.front().first;
            y=q.front().second;
            q.pop();
            for(auto it :v)
            {
                int row=it.first+x;
                int col=it.second+y;
                if(row>=0 && row<m &&col>=0 && col<n && grid[row][col]=='1' && !visited[row][col])
                {
                    visited[row][col]=true;
                    q.push({row,col});
                }
            }
        }
        
    }
    int numIslands(vector<vector<char>>& grid) {
       visited.resize(grid.size(),vector<bool>(grid[0].size(),false));
       int ans=0;
       for(int i=0;i<grid.size();i++)
       {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]=='1' && !visited[i][j])
                {
                    ans++;
                    bfs(grid,i,j);
                }
            }
       }
       return ans;
    }
};
