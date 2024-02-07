#include <string>
#include <algorithm> 
#include <iostream>

using namespace std;
class Solution {
public:
    string frequencySort(string s) {
        int* countFreqs = new int[26];
        for(auto& k:s) countFreqs[k - 'a']++;
        cout << countFreqs[0] << endl;
        return "hello";
    }
};

int main(){
    string s = "helloworld";
    cout << Solution().frequencySort(s) << endl;
}