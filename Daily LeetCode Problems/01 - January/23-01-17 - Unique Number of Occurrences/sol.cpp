#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> m;
        for(int i:arr) m[i]++;
        unordered_set<int> s;
        for(auto i:m){
            int freq = i.second;
            if(s.find(freq)!=s.end()) return false;
            s.insert(freq);
        }
        return true;
    }
};