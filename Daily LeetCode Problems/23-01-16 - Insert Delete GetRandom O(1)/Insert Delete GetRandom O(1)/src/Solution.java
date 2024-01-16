import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

class RandomizedSet {
    HashMap<Integer, Integer> map;
    List<Integer> values;
    Random rand = new Random();

    public RandomizedSet() {
        this.map = new HashMap<>();
        this.values = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        if(this.map.keySet().contains(val)) return false;
        this.map.put(val, this.values.size());
        this.values.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if(!this.map.keySet().contains(val)) return false;
        
        int idx = map.get(val);
        int last = values.get(values.size() - 1);
        
        values.set(idx, last);
        map.put(last, idx);
        
        values.remove(values.size() - 1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        return values.get(rand.nextInt(values.size()));
    }
}

