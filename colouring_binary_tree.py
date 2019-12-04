# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.res=False
        
        def fsize(root):
            if not root:
                return 0
            return 1+fsize(root.left)+fsize(root.right)
        def findans(root,x):
            if not root:
                return
            if root.val==x:
                l_s=fsize(root.left)
                r_s=fsize(root.right)
                p_s=n-l_s-r_s-1
                if l_s>r_s+p_s+1 or r_s>l_s+p_s+1 or p_s>l_s+r_s+1:
                    self.res=True
            else:
                findans(root.left,x)
                findans(root.right,x)
        findans(root,x)
        return self.res
