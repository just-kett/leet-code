#include <cctype>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        if (s == "") {
            return true;
        }
        else {
            string sr = "";
            string rs = "";
            for (char c : s) {
                if (isalnum(c)) {
                    sr += tolower(c);
                }
            }
            for (int i = sr.length() - 1; i >= 0; i -= 1) {
                rs += sr[i];
            }
            if (sr == rs) {
                return true;
            }
            else {
                return false;
            }
        }
    }
};