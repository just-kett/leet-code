#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        vector<int> seq;
        for (int x : nums) {
            auto k = lower_bound(seq.begin(), seq.end(), x);
                if (k == seq.end()) {
                    seq.push_back(x);
            }
            else {
                *k = x;
            }
        }
        return seq.size();
    } 
};