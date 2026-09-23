#include <vector>
#include <string> 

using namespace std;

class Solution {
public:

    int maxActiveSectionsAfterTrade(string s) {   
        int start = 0;
        int length = -1;
        int max_length = -1;
        int sum = 0;
        vector<string> l;
        for (int i = 0; i < s.length(); i++) {
            if (s[start] != s[i]) {
                length = i - start;
                string str = s.substr(start, length);
                l.push_back(str);
                start = i;
            }
        }
        l.push_back(s.substr(start));
        for (int j = 0; j < l.size(); j++) {
            if (l[j][0] == '1' && j-1>=0 && stoi(l[j-1]) == 0 && j+1<l.size() && stoi(l[j+1]) == 0) {
                length = l[j-1].length() + l[j+1].length();
                if (length > max_length) {
                    max_length = length;
                }
            }
        }
        for (char j : s) {
            if (j == '1') {
                sum += 1;
            }
        }
        return sum + max_length;
    }
};