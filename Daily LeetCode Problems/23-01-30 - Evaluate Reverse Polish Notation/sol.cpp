#include <string> 
#include <deque>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    unordered_set<string> operators = {"+", "-", "*", "/"};

    int evalRPN(vector<string>& tokens) {
        deque<int> stack;
        
        for(auto& t:tokens){
            if(operators.find(t) != operators.end()){
                int b = stack.back();
                stack.pop_back();
                int a = stack.back();
                stack.pop_back();

                if(t == "/") stack.push_back(a / b);
                else if(t == "*") stack.push_back(a * b);
                else if(t == "-") stack.push_back(a - b);
                else if(t == "+") stack.push_back(a + b);
            }

            else stack.push_back(stoi(t));
        }

        return stack.back();
    }
};