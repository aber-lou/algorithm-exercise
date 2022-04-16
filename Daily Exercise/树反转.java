class TreeNode {
    TreeNode left;
    TreeNode right;
    int val;
}

class Solution {
    TreeNode inverTree(TreeNode root) {
        if (root == null) return null;

        TreeNode left = inverTree(root.left);
        TreeNode right = inverTree(root.right);

        root.left = right;
        root.right = left;

        return root
    }
}