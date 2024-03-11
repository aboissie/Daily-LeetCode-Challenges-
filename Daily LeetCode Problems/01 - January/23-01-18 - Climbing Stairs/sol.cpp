#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<int, int> map = { {1, 1}, {2, 2}};

    int climbStairs(int n) {
        if(map.find(n)!=map.end()) return map[n];
        map[n] = climbStairs(n - 1) + climbStairs(n - 2);
        return map[n];
    }
};