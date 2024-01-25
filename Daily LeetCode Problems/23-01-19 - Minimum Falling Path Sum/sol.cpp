#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        for(int r = 1; r < matrix.size(); r++){
            for(int c = 0; c < matrix[0].size(); c++){
                if(c==0) matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1]);
                else if(c==matrix[0].size()-1) matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1]);
                else matrix[r][c] += min(min(matrix[r-1][c], matrix[r-1][c-1]), matrix[r-1][c+1]);
            }
        }

        return *min_element(matrix[matrix.size()-1].begin(), matrix[matrix.size()-1].end());
    }
};