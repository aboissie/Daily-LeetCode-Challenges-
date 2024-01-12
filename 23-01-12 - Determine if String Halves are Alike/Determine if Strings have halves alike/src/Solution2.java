import java.util.Set;
import java.util.HashSet;

public class Solution2 {
    public String vowels = "aeiouAEIOU";

    private int countVowel(int start, int end, String s){
        int res = 0;
        for(int i = start; i < end; i++){
            if(vowels.indexOf(s.charAt(i)) != -1) res++;
        }
        return res;
    }
    
    public boolean halvesAreAlike(String s) {
        return countVowel(0, s.length()/2, s) == countVowel(s.length()/2, s.length(), s);
    }
}
