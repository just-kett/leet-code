#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> result;
    void backtrack(string& path, int open, int close, int n) {
        if (path.size() == 2*n) {
            result.push_back(path);
            return;
        }
        if (open < n) {
            path.push_back('(');
            backtrack(path, open + 1, close, n);
            path.pop_back();
        }
        if (close < open) {
            path.push_back(')');
            backtrack(path, open, close + 1, n);
            path.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        int open = 0;
        int close = 0;
        string path = "";
        backtrack(path, open, close, n);
        return result;
    }
};