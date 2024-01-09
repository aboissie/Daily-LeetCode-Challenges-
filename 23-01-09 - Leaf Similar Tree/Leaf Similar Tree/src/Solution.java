import java.util.LinkedList;
import java.util.Vector;

class Solution {
    private static Vector<Integer> bfs(TreeNode root){
        LinkedList<TreeNode> Q = new LinkedList<>();
        Q.add(root);
        
        Vector<Integer> res = new Vector<>();

        while(!Q.isEmpty()){
            TreeNode v = Q.poll();

            if(v.left == null & v.right == null){
                res.add(v.val);
                continue;
            }
            
            
            if(v.right!=null) Q.addFirst(v.right);
            if(v.left!=null) Q.addFirst(v.left);
            
        }
        
        return res;
    }

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        return bfs(root1).equals(bfs(root2));
    }
}