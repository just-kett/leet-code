class Solution {
public:

    vector<int> maxDepthAfterSplit(string seq) {
        int len = seq.size();
        std::vector<int> result(len, -1);



        bool current_A = true;
        while (std::find(result.begin(), result.end(), -1) != result.end()) {
            if (current_A) {
                bool cur = true;

                for(int i = 0; i < len; i++) {
                    if ((cur) && (seq[i] == '(')) {
                        result[i] = 0;
                        seq[i] = '0';
                        cur = false;
                    }
                    else if ((!cur) && (seq[i] == ')')) {
                        result[i] = 0;
                        cur = true;
                        seq[i] = '0';
                    }
                }
                current_A = false;
            }
            else {
                bool cur = true;
                    for(int i = 0; i < len; i++) {
                        if ((cur) && (seq[i] == '(')) {
                            result[i] = 1;
                            seq[i] = '0';
                            cur = false;
                        }
                        else if ((!cur) && (seq[i] == ')')) {
                            result[i] = 1;
                            cur = true;
                            seq[i] = '0';
                    }
                }
                current_A = true;
            }
        }
        return result;
        
    }
};