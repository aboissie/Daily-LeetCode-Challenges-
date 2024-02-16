#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        vector<vector<string>> result;

        for(const auto& s:strs){
            string tmp = s; 
            sort(tmp.begin(), tmp.end());
            res[tmp].push_back(s);
        }
        
        for(const auto& [_, item]: res) result.push_back(item);
    
        return result;
    }
};