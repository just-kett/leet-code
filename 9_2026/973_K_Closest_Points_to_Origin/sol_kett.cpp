#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<pair<vector<int>, float>> arr;
        vector<vector<int>> final;
        for (auto i : points) {
            float m = sqrt(i[0]*i[0] + i[1]*i[1]);
            arr.push_back({i, m});
        }
        sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;});
        for (int j = 0; j < k; j++) {
            final.push_back(arr[j].first);
        }
        return final;        
    }
};