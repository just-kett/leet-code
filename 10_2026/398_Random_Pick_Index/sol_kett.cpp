#include <vector>
#include <cstdlib>

using namespace std;

class Solution {
private:
    vector<int> nums;

public:
    Solution(vector<int>& nums) {
        this->nums = nums;
    }

    int pick(int target) {
        vector<int> kq;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                kq.push_back(i);
            }
        }

        int randomIndex = rand() % kq.size();
        return kq[randomIndex];
    }
};