#include <queue>

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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> q;
        TreeNode* current = root;
        q.push(current);
        bool even = true;

        while(!q.empty()){
            int size = q.size();

            int prev = -1;
            if(even) prev = 1000000;

            while(size > 0){
                TreeNode* current = q.front();
                q.pop();

                if(even && (current->val <= prev || current->val%2==0)) return false;
                if(!even && (current->val >= prev || current->val%2==1)) return false;

                size--;

                if(current->left) q.push(current->left);
                if(current->right) q.push(current->right);
            }

            even = !even;
        }

        return true;
    }
};