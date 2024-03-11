#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        auto ans = 0, prev_number_of_one = 0; int number_of_one;
        for(auto &row : bank){
            number_of_one = std::count(row.begin(), row.end(), '1');
            if(number_of_one != 0){
                ans += number_of_one * prev_number_of_one;
                prev_number_of_one = number_of_one;
            }
        }
        return ans;
    }
};