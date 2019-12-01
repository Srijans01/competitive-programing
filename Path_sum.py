# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val==sum:
                return True
            else:
                return False
        sum-=root.val
        if root.left and root.right:
            return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        elif root.left:
            return self.hasPathSum(root.left,sum)
        elif root.right:
            return self.hasPathSum(root.right,sum)
