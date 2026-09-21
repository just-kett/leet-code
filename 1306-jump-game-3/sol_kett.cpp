#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        queue<int> q;
        vector<bool> visited(arr.size(), false);
        
        q.push(start);
        visited[start] = true;

        while(!q.empty()) {
            int current = q.front();
            q.pop();

            if (arr[current] == 0) {
                return true;
            }

            int right = current + arr[current];
            int left = current - arr[current];

            if (right <= arr.size()-1 && visited[right] != true) {
                visited[right] = true;
                q.push(right);
            }
            if (left >= 0 && visited[left] != true) {
                visited[left] = true;
                q.push(left);
            }
        }
        return false;
    }
};
    