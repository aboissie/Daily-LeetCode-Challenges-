# include <vector> 
# include <algorithm>
# include <unordered_map>
using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> mapper;
        for(int n:nums) mapper[n]++;
        int maxCount = INT32_MIN;
        int res = 0;
        for(auto& [k,v]: mapper){
            if(v==maxCount) res+=v;
            else if(v>maxCount){
                res = v;
                maxCount = v;
            }
        }

        return res;
    }
};