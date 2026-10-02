class Solution {
public:
    vector<string>v;
    vector<string>pick{"(",")"};
    void backtrack(int n, string& s, int x, int y)
    {
        if(x+y==2*n)
        {
            v.push_back(s);
            return;
        }
        if(x<n)
        {
            s+="(";
            backtrack(n,s,x+1,y);
            s.pop_back();
        }
        if(y<x)
        {
            s+=")";
            backtrack(n,s,x,y+1);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        string s;
        backtrack(n,s,0,0);
        return v;
    }
};