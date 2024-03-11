struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int leftmost = 0;
    int leftmostrow = -1;
    
    void visit(TreeNode* root, int depth){
        if(root==nullptr) return;
        if(depth > leftmostrow){
            leftmost = root->val;
            leftmostrow = depth;
        }
        visit(root->left, depth + 1);
        visit(root->right, depth + 1);
    }

    int findBottomLeftValue(TreeNode* root) {
        visit(root, 0);
        return leftmost;
    }
};