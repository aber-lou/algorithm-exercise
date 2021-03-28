class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root:TreeNode):
        self.nodelist = []
        self.index = -1
        self.midorder(root)


    def midorder(self,root):
        if  root:
            self.midorder(root.left)
            self.nodelist.append(root.val)
            self.midorder(root.right)
        

    def next(self) -> int:
        self.index += 1
        nextVal = self.nodelist(self.index)
        return nextVal

    def haxNext(self) -> bool:
        if self.index < len(self.nodelist) - 1:
            return True
        return False
