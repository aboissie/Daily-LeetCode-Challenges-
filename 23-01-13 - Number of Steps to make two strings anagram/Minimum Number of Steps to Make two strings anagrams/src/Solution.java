import java.util.HashMap;

class Solution {
    public int minSteps(String s, String t) {
        if(s.length() != t.length()) throw new Error();

        HashMap<Character, Integer> counter = new HashMap<>();
        for(Character c: s.toCharArray()){
            if(counter.containsKey(c)) counter.put(c, counter.get(c) + 1);
            else counter.put(c, 1);
        }

        for(Character c: t.toCharArray()){
            if(counter.containsKey(c) && counter.get(c) > 0) counter.put(c, counter.get(c) - 1);
        }
        
        int res = 0;
        for(int val:counter.values()) res+=val;
        return res;
    }
}