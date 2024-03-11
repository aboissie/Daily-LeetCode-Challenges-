#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
using namespace std;

class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        int k = 0;
        sort(nums.begin(), nums.end(), greater<int>());
        
        while(nums[k] >= accumulate(nums.begin() + k + 1, nums.end(), 0LL)){
            k += 1;
            if(k == nums.size()) return -1;
        }

        return accumulate(nums.begin() + k, nums.end(), 0LL);
    }
};

int main(){
    vector<int> nums = {1,12,1,2,5,50,3};
    cout << Solution().largestPerimeter(nums) << endl;
    return -1;
};