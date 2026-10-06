#include <string>

using namespace std;

class Solution {
public:
    int minAddToMakeValid(string s) {
        int close = 0;
        int open = 0;
        for (char c : s) {
            if (c == '(') {
                open += 1;
            }
            else {
                if (open > 0) {
                    open -= 1;
                }
                else {
                    close += 1;
                }
            }
        }
        return open + close;
    }
};