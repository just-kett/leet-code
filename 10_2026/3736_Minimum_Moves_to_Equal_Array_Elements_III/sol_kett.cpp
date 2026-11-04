#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        int output = 0;
        for (int i = 1; i < nums.size(); i++) {
            output += nums[0] - nums[i];
        }
        return output;
    }
};