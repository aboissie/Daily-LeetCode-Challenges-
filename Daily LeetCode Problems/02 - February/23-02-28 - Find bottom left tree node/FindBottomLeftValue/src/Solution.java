import java.util.HashMap;
import java.util.List;
import java.util.Vector;

class Solution {
    public HashMap<Integer, Integer> levelOrder = new HashMap<>();

    public int findBottomLeftValueHelper(TreeNode root, int depth) {
        if(!(root == null)){
            if(!levelOrder.keySet().contains(depth)) this.levelOrder.put(depth, root.val);
            findBottomLeftValueHelper(root.left, depth + 1);
            findBottomLeftValueHelper(root.right, depth + 1);
        }
        return -1;
    }

    public int findBottomLeftValue(TreeNode root) {
        findBottomLeftValueHelper(root, 0);
        int s = 0;
        for(int k: levelOrder.keySet()) s = k;
        return levelOrder.get(s);
    }
}

