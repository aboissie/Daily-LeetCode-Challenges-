#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    int minSteps(string s, string t) {
        int sval[26] = {0};
        for(char Cs:s) sval[Cs - 'a'] += 1;
        for(char Ct:t) sval[Ct - 'a'] -= 1;
        return accumulate(begin(sval), end(sval), 0, plus<int>());
    }
};