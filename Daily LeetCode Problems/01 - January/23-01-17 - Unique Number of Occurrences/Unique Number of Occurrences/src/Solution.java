import java.util.HashMap;
import java.util.HashSet;
import java.util.Collection;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i:arr) map.put(i, 1 + map.getOrDefault(i, 0));
        
        HashSet<Integer> set = new HashSet<>();
        for(int i:map.values()) {
            if(set.contains(i)) return false;
            set.add(i);
        }
        return true;
    }
}