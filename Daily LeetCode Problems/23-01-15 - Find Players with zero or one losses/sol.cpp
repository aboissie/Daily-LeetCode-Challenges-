# include <vector>
# include <algorithm>
# include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> lossCount;
        for(vector<int>& match:matches){
            if(lossCount.find(match[1]) != lossCount.end()) lossCount.at(match[1]) += 1;
            else lossCount.insert(make_pair(match[1], 1));
            if(lossCount.find(match[0]) == lossCount.end()) lossCount.insert(make_pair(match[0], 0));
        }

        vector<int> zeroLoss;
        vector<int> oneLoss;
        for(const auto& pair: lossCount){
            if(pair.second == 0) zeroLoss.push_back(pair.first);
            if(pair.second == 1) oneLoss.push_back(pair.first);
        }

        std::sort(zeroLoss.begin(), zeroLoss.end(), less<int>());
        std::sort(oneLoss.begin(), oneLoss.end(), less<int>());
        
        vector<vector<int>> res;
        res.push_back(zeroLoss);
        res.push_back(oneLoss);
        return res;
        
    }
};