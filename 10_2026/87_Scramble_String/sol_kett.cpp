#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<string, bool> memo;
    bool isScramble(string s1, string s2) {
        if (s1 == s2) {
            return true;
        }
        int n = s1.length();
        string key = s1 + "_" + s2;
        if (memo.count(key)) {
            return memo[key];
        }
        for (int i = 1; i < n; i++) {
            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && 
                isScramble(s1.substr(i), s2.substr(i))) {
                return memo[key] = true;
            }
            if (isScramble(s1.substr(0, i), s2.substr(n - i)) && 
                isScramble(s1.substr(i), s2.substr(0, n - i))) {
                return memo[key] = true;
            }
        }
        return memo[key] = false;
    }
};