#include <vector> 
#include <algorithm>
#include <iostream> 

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        for(int* n:nums) *n = (*n) * (*n);
        sort(nums.begin(), nums.end());
        return nums;
    }
};

int main(){
    vector<int> nums = {-5, -2, -1, 0, 1, 2, 4, 6};
    vector<int> res = Solution().sortedSquares(nums);
    for(int n:res){
        std::cout << n << " ";
    }   
    return -1;
}