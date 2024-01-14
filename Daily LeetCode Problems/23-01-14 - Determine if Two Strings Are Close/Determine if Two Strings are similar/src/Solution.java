import java.util.Collection;
import java.util.HashMap;

class Solution {
    private static HashMap<Character, Integer> Counter(String word){
        HashMap<Character, Integer> freqCounter = new HashMap<>();
        for(Character c: word.toCharArray()){
            if(freqCounter.containsKey(c)) freqCounter.put(c, freqCounter.get(c) + 1);
            else freqCounter.put(c, 1);
        }
        return freqCounter;
    }

    public boolean closeStrings(String word1, String word2) {
        HashMap<Character, Integer> freqCounter1 = Counter(word1);
        HashMap<Character, Integer> freqCounter2 = Counter(word2);
        
        Integer[] res1 = new Integer[freqCounter1.values().size()];
        Integer[] res2 = new Integer[freqCounter2.values().size()];
        Integer[] freq1 =  freqCounter1.values().toArray(res1);
        Integer[] freq2 =  freqCounter2.values().toArray(res2);

        Arrays.sort(freq1);
        Arrays.sort(freq2);

        return freq1 == freq2;
    }
}