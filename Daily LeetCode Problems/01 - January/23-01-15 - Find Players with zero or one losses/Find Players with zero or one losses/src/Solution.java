import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Collections;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, Integer> lossCount = new HashMap<>();

        // Initialize all players with 0 losses
        for (int[] match : matches) {
            lossCount.putIfAbsent(match[0], 0);
            lossCount.putIfAbsent(match[1], 0);
        }

        // Count losses
        for (int[] match : matches) {
            lossCount.put(match[1], lossCount.get(match[1]) + 1);
        }

        ArrayList<Integer> zeroLoss = new ArrayList<>();
        ArrayList<Integer> oneLoss = new ArrayList<>();

        // Distribute players into zeroLoss and oneLoss lists
        for (Integer player : lossCount.keySet()) {
            int losses = lossCount.get(player);
            if (losses == 0) {
                zeroLoss.add(player);
            } else if (losses == 1) {
                oneLoss.add(player);
            }
        }

        // Sort the lists
        Collections.sort(zeroLoss);
        Collections.sort(oneLoss);

        ArrayList<List<Integer>> res = new ArrayList<>();
        res.add(zeroLoss);
        res.add(oneLoss);
        return res;
    }
}
