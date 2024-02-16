#include <bits/stdc++.h> 
#include <string>
#include <algorithm> 
#include <iostream>

using namespace std;
class Solution {
public:
    bool cmp(pair<char, int>& a, pair<char, int>& b){return a.second < b.second;}
    
    void sort(map<char, int>& M){
        vector<pair<char, int>> A;

        for(auto& it: M){
            A.push_back(it);
        }    

        sort(A.begin(), A.end(), cmp);
    }

    string frequencySort(string s) {
        map<char, int> freqCount;
        for(char c:s){
            freqCount[c]++;
        }
        sort(freqCount);
        
        string res = "";
        for(auto& [k,v]: freqCount){
            res += string(v, k);
        }
        
        return res;
    }
};

int main(){
    string s = "helloworld";
    cout << Solution().frequencySort(s) << endl;
}