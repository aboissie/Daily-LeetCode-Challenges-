#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(), greater<int>());
        int res = 0; 

        for(int i = 0; i < citations.size(); i++){
            if(citations[i] >= res) res++;
        }
        return res;
    }
};