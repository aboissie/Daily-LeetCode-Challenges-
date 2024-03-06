# include <string>

using namespace std;

class Solution {
public:
    int minimumLength(string s) {
        int l = 0, r = s.size() - 1;
        while(s[l] == s[r]){
            char c = s[l];
            while(l <= r && s[l] == c) l++;
            while(l <= r && s[r] == c) r--;
            if(l > r) return 0;
        }
        return r - l + 1;
    }
};