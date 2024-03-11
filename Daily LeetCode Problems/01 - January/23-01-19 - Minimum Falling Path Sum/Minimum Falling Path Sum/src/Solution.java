import java.util.Collections;
import java.util.Arrays;

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        // Loop through each element in the matrix, and modify iteratively, such that 
        // m[r][c] = min(m[r-1][c-1], m[r-1][c], m[r-1][c+1]) + m[r][c]
        for(int r = 1; r < matrix.length; r++){
            for(int c = 0; c < matrix[0].length; c++){
                if(c==0) matrix[r][c] += Math.min(matrix[r-1][c], matrix[r-1][c + 1]);
                else if(c==matrix[0].length - 1) matrix[r][c] += Math.min(matrix[r-1][c - 1], matrix[r-1][c]);
                else matrix[r][c] += Math.min(Math.min(matrix[r-1][c - 1], matrix[r-1][c]), matrix[r-1][c + 1]);
            }
        }

        int min = Integer.MAX_VALUE;
        for(int val: matrix[matrix.length - 1]) min = Math.min(min, val);
        return min;
    }
}