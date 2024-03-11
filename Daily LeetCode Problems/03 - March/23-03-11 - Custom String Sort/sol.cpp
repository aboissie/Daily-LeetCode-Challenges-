#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string customSortString(string order, string s) {
        int freqCount[26];
        for(char c:s) freqCount[c - 'a']++;

        string res = "";

        for(char c:order){ 
            res += string(freqCount[c - 'a'], c);
            freqCount[c - 'a'] = 0;
        }

        for(int i = 0; i < 26; i++){
            res = res + string(freqCount[i + 'a'], c);
        }

        return res;
    }
};