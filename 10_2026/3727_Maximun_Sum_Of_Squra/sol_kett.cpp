#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        vector<long long> square;
        long long sum = 0;
        int left = 0;
        int right = nums.size() - 1;
        for (int i : nums) {
            square.push_back(i*i);
        }
        sort(square.begin(), square.end());
        for (int j = 0; j < nums.size(); j++) {
            if (j % 2 == 0) {
                sum += square[right];
                right -= 1;
            }
            else {
                sum -= square[left];
                left += 1;
            }
        }
        return sum;
    }
};