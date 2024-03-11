#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());

        std::vector<int> res;
        for(const auto& num: nums2){
            if(set1.count(num)){
                res.push_back(num);
                set1.erase(num);
            }
        }
        
        return res;
    }
};