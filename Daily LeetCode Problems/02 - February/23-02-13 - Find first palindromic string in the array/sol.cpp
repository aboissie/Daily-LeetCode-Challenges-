#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(string& s:words){
            bool pal = true;
            for(int i = 0; i < s.length / 2; i ++){
                if(s[i] != s[s.length - i]){pal = false; break;}
            }
            if(pal) return s;
        }
        return "";
    }
};