#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(), logs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int q_len = queries.size();
        vector<pair<int, int>> sorted_queries(q_len);
        for (int i = 0; i < q_len; i++) {
            sorted_queries[i] = {queries[i], i};
        }
        sort(sorted_queries.begin(), sorted_queries.end());

        vector<int> ans(q_len);
        vector<int> cnt(n + 1, 0); 
        int active = 0;           
        int left = 0, right = 0;
        int l_len = logs.size();

        for (const auto& [q_time, orig_idx] : sorted_queries) {
            while (right < l_len && logs[right][1] <= q_time) {
                int srv_id = logs[right][0];
                if (cnt[srv_id] == 0) {
                    active++; 
                }
                cnt[srv_id]++;
                right++;
            }

            while (left < l_len && logs[left][1] < q_time - x) {
                int srv_id = logs[left][0];
                cnt[srv_id]--;
                if (cnt[srv_id] == 0) {
                    active--; 
                }
                left++;
            }

            ans[orig_idx] = n - active;
        }

        return ans;
    }
};
