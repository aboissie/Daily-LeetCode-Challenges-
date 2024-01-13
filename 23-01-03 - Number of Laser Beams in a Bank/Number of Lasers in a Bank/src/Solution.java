class Solution {
    private static int countOnes(String row){
        int res = 0;
        for(Character s: row.toCharArray()) res += (s=='1')? 1:0;
        return res;
    }
    public int numberOfBeams(String[] bank) {
        int s = countOnes(bank[0]);
        int res, tmp = 0, 0;
        for(int i = 1; i < bank.length; i ++){
            if(countOnes(bank[i]) == 0) continue;
            tmp = countOnes(bank[i]);
            res += s * tmp;
            s = tmp;
        }
        return res;
    }
}