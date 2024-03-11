#include <algorithm>
#include <string>

using namespace std;

class Solution {
private:
    static int countZeros(string row){
        int res = 0;
        for(char c:row) res += c - '0';
        return res;
    }

public:
    int numberOfBeams(vector<string>& bank) {
        int res = 0;
        int currLasers = countZeros(bank.at(0));
        for(int i = 1; i < bank.size(); i++){
            int tmp = countZeros(bank.at(i));
            if(tmp == 0) continue;
            res += tmp * currLasers;
            currLasers = tmp;
        }
        return res;
    }
};