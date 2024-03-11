import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean halvesAreAlike(String s) {
       Set<Character> vowels = new HashSet<>(Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        
        int c1 = 0;
        int c2 = 0;
        for(int i = 0; i < s.length()/2; i++) if(vowels.contains(s.charAt(i))) c1+=1;
        for(int i = s.length()/2; i < s.length(); i++) if(vowels.contains(s.charAt(i))) c2+=1;

        return c1 == c2;
    }
}