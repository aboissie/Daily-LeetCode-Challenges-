import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        TreeNode current = root;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(current);
        boolean even = true;
        
        while(!q.isEmpty()){
            int size = q.size();
            
            int prev = Integer.MAX_VALUE;
            if(even) prev = Integer.MIN_VALUE;

            while(size > 0){
                current = q.poll();
                if((even && (current.val % 2==0 || current.val < prev)) || (!even && (current.val % 2 ==1 || current.val >= prev))){
                    return false;
                }
                prev = current.val;
                if(current.left != null) q.add(current.left);
                if(current.right != null) q.add(current.right);
                size--;
            }
            even = !even;
        }
        return true;
    }
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
    }
}

