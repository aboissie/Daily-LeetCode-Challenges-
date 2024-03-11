#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

class Solution {
public:
    vector<int> givePerfectSquares(int n){
        vector<int> res;
        for(int i = 1; i * i <= n; i++) res.push_back(i * i);
        return res;
    }
    
    int numSquaresHelper(int n, unordered_map<int, int>& dic){ // Pass dic by reference
        if(dic.find(n) != dic.end()) return dic[n];
        dic[n] = INT_MAX;
        vector<int> perfSquares = givePerfectSquares(n);
        for(int k: perfSquares){
            if (n - k >= 0) {
                int count = numSquaresHelper(n - k, dic);
                dic[n] = min(dic[n], 1 + count);
            }
        }

        return dic[n];
    }

    int numSquares(int n) {
        unordered_map<int, int> dic;
        dic[0] = 0;
        dic[1] = 1;
        return numSquaresHelper(n, dic);
    }
};

int main() {
    Solution sol;
    
    // Test cases
    int testCases[] = {12, 8, 35};
    for (int n : testCases) {
        cout << "Minimum number of perfect squares for " << n << ": " << sol.numSquares(n) << endl;
    }
    
    return 0;
}
