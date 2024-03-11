import java.util.PriorityQueue;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> jumps = new PriorityQueue<>();
        int n = heights.length;
        for(int i = 0; i < n - 1; i++){
            int diff = heights[i + 1] - heights[i];
            if(diff > 0) jumps.add(diff);
                        
            if(jumps.size() > ladders && !jumps.isEmpty()){
                bricks -= jumps.remove();
            }

            if(bricks < 0) return i;
        }

        return n - 1;
    }
}