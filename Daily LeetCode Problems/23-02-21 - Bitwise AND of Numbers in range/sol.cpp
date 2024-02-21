#include <iostream>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int a = 0;
        while(left < right){
            left >>= 1;
            right >>=1;
            a += 1;
        }
        return left << a;
    }
};

int main(){
    cout << Solution().rangeBitwiseAnd(5, 7) << endl;
}