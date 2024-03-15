#include <vector> 

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int arrf = 1;
        vector<int> res(1, nums.size());
        for(int i = 0; i < nums.size(); i++){
            res[i] *= arrf;
            arrf *= nums[i];
        }

        arrf = 1;
        for(int i = nums.size() - 1; i > - 1; i--){
            res[i] *= arrf;
            arrf *= nums[i];
        }

        return res;
    }
};