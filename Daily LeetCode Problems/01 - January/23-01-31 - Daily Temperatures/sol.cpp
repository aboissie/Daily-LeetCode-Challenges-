#include <iostream>
#include <stack> 
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<int> stack; 

        for(int i = 0; i < temperatures.size(); i++){
            while(stack.size() > 0 && temperatures[stack.top()] < temperatures[i]){
                res[i - stack.top()] = stack.top();
                stack.pop();
            }
            stack.push(i);
        }
        return res;
    }
};