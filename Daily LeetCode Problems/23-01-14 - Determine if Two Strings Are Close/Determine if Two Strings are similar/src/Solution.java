import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;

class Solution {
    private static HashMap<Character, Integer> Counter(String word){
        HashMap<Character, Integer> freqCounter = new HashMap<>();
        for(Character c: word.toCharArray()){
            freqCounter.put(c, freqCounter.getOrDefault(c, 0) + 1);
        }
        return freqCounter;
    }

    public boolean closeStrings(String word1, String word2) {
        HashMap<Character, Integer> freqCounter1 = Counter(word1);
        HashMap<Character, Integer> freqCounter2 = Counter(word2);

        // Check if both words have the same set of characters
        if (!freqCounter1.keySet().equals(freqCounter2.keySet())) {
            return false;
        }

        Integer[] freq1 = freqCounter1.values().toArray(new Integer[0]);
        Integer[] freq2 = freqCounter2.values().toArray(new Integer[0]);

        Arrays.sort(freq1);
        Arrays.sort(freq2);

        return Arrays.equals(freq1, freq2);
    }
}
