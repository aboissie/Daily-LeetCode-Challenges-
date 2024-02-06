#include <unordered_map> 
#include <vector> 
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<int, vector<string>> res;
        int minV = INT_MAX;
        for(int i = 0; i < list1.size(); i++){
            auto findIdx = std::find(list2.begin(), list2.end(), list1[i]); 
            if(findIdx != list2.end()){
                res[i + std::distance(list2.begin(), findIdx)].push_back(list1[i]);
                minV = min(minV, i + (int) std::distance(list2.begin(), findIdx));
            }
        }
        
        return res[minV];
    }
};