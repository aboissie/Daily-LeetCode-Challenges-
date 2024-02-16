#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> buildCounter(vector<int>& arr){
        unordered_map<int, int> res;
        for(int i:arr) res[i] += 1;

        vector<int> counts;
        for(pair<int, int> p:res) counts.push_back(p.second); 

        return counts;
    }

    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        vector<int> freqCount = buildCounter(arr);
        sort(freqCount.begin(), freqCount.end());
        
        int remaining = freqCount.size();
        int value = k;
        
        for(int freq:freqCount){
            if(value >= freq){
                value -= freq;
                remaining -= 1;
            }
            else break;
        }

        return remaining;
    }
};

int main(){
    vector<int> arr = {4,3,1,1,3,3,2};
    cout << Solution().findLeastNumOfUniqueInts(arr, 3);
};