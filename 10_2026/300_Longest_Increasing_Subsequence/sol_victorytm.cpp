#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        tails.push_back(nums[0]);
        for(int i:nums){
            if(tails.empty() || i>tails.back()){
                tails.push_back(i);
            }
            else{
                auto it = lower_bound(tails.begin(),tails.end(),i);
                //position where value is greater or equal to i
                int pos = it - tails.begin();
                tails[pos] = i;
            }
        }
        return tails.size();
    }
};