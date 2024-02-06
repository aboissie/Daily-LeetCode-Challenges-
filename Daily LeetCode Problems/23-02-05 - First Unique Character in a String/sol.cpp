#include <string>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        int charCount[26] = {0};
        for(int i = 0; i < s.size(); i++) charCount[s[i] - 'a']++;
        for(int i = 0; i < s.size(); i++){
            if(charCount[s[i] - 'a']==1) return i;
        }
        return -1;
    }
};