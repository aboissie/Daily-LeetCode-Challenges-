#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res = {{nums[0]}};

        for(int i = 1; i < nums.size(); i++){
            int num = nums[i];
            vector<int> currentBucket = res.back();
            
            if(currentBucket.size() == 3){
                res.push_back({num}); 
                continue;
            }

            if(num > currentBucket[0] + k) return {};
            
            res.pop_back();
            currentBucket.push_back(num);
            res.push_back(currentBucket);
        }

        if(res.back().size()<3) return {};
        return res;
    }
};