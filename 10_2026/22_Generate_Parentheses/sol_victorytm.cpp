#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <utility>
#include <algorithm>

using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        stack<tuple<int,int,string>> stakk; vector<string> ans;
        stakk.push({n,n,string("")});
        while(!stakk.empty()){
            auto [f,s,t] = stakk.top();
            stakk.pop();
            if(f == 0 && s == 0){
                ans.push_back(t);
                continue;
            }
            if(s > 0){
                if(f > 0)
                    stakk.push({f-1,s,t+"("});
                if(f < s)
                    stakk.push({f,s-1,t+")"});
            }
        }
        return ans;
    }
};