#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int desc = 1;
        int incr = 1;
        int start = nums[0];
        vector<int> sum;
        if (nums.size() == 1) {
            return 1;
        }
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < start) {
                desc += 1;
                sum.push_back(desc);
                incr = 1;
                start = nums[i];
            }
            else if (nums[i] > start) {
                incr += 1;
                sum.push_back(incr);
                desc = 1;
                start = nums[i];
            }
            else {
                sum.push_back(1);
                desc = 1;
                incr = 1;
            }
        }
        sort(sum.begin(), sum.end());
        return sum.back();
    }
};