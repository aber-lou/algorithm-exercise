class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self. right = right
    
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float('inf')
        self.pre = -1

        def dfs_LNR(tree:TreeNode) -> None:
            if tree == None: return
            dfs_LNR(tree.left)

            if self.pre != -1:
                self.res = min(self.res,tree.val - self.pre)
            self.pre = tree.val

            dfs_LNR(tree.right)
        

        dfs_LNR(root)
        return self.res

