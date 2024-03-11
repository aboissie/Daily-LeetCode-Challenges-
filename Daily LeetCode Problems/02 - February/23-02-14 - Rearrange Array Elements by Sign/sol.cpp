#include <vector> 
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        deque<int> posVals;
        deque<int> negVals;

        for(int i:nums){
            if(i<0) negVals.push_back(i);
            else posVals.push_back(i);
        }

        for(int i = 0; i < nums.size(); i+=2){
            nums[i] = posVals.front();
            nums[i+1] = negVals.front();

            posVals.pop_front();
            negVals.pop_front();
        }
        
        return nums;
    }
};