class Solution {
    private static int helperDiff(TreeNode root, int currmin, int currmax){
        if(root == null) return currmax - currmin;
        currmax = Math.max(currmax, root.val);
        currmin = Math.min(currmin, root.val);

        int left = helperDiff(root.left, currmin, currmax);
        int right = helperDiff(root.right, currmin, currmax);

        return Math.max(left, right);
        
    }
    
    public int maxAncestorDiff(TreeNode root) {
        if(root == null) return 0;
        return helperDiff(root, root.val, root.val);
    }
}