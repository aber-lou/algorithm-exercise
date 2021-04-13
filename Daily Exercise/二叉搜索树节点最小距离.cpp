class Solution {
public:
    void dfs(TreeNode *root, int &pre, int& mins) {
        if (root == nullptr) {
            return;
        }
        dfs(root->left, pre, mins);
        if (pre == -1) {
            pre = root->val;
        }else {
            mins = min(mins, root->val - pre);
            pre = root->val;
        }
        dfs(root->right, pre ,mins);
    }

    int minDiffInBST(TreeNode* root) {
        int mins = INT_MAX, pre = -1;
        dfs(root, pre, mins);
        return mins;
    }
};