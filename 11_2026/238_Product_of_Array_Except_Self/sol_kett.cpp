#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int numzero = 0;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                numzero += 1;
            }
            else {
                product *= nums[i];
            }
        }
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] == 0 && numzero >= 2) {
                result.push_back(0);
            }
            else if (nums[j] == 0 && numzero == 1) {
                result.push_back(product);
            }
            else if (nums[j] != 0 && numzero >= 1) {
                result.push_back(0);
            }
            else if (numzero == 0) {
                result.push_back(product / nums[j]);
            }
        }
        return result;
    }
};