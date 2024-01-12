#include <algorithm>
using namespace std;

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
    int diff = INT_MIN;

    void maxDiffhelper(TreeNode* root, int currmin, int currmax){
        if(root == NULL) return;
       
        currmax = max(currmax, root->val);
        currmin = min(currmin, root->val);
        
        diff = max(diff, currmax - currmin);

        maxDiffhelper(root->left, currmin, currmax);
        maxDiffhelper(root->right, currmin, currmax);
    }

    int maxAncestorDiff(TreeNode* root) {
        if(!root) return 0;
        int mx = INT_MIN, mi = INT_MAX;
        maxDiffhelper(root, mi, mx);
        
        return diff;
    }
};