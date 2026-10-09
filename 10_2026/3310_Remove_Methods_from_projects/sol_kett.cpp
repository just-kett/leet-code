#include <vector>

using namespace std;

class Solution {
public:
    vector<bool> visited;
    vector<vector<int>> adj;
    vector<int> results;
    void dfs(int u) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        visited.assign(n, false);
        adj.assign(n, vector<int>());
        for (auto c : invocations) {
            int u = c[0];
            int v = c[1];
            adj[u].push_back(v);
        }
        dfs(k);
        bool cut = true;
        for (auto r : invocations) {
            if (visited[r[0]] == false && visited[r[1]] == true) {
                cut = false;
                break;
            }
        }
        for (int i = 0; i < n; i++) {
            if (!cut || visited[i] == false) {
                results.push_back(i);
            } 
        }
        return results;
    }
};