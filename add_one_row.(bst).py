# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return TreeNode(v)
        if d==1:
            new_node=TreeNode(v)
            new_node.left=root
            return new_node
        self.addUtil(root,1,d,v)
        return root
    def addUtil(self,c_n,c_l,d,v):
        if not c_n or d<c_l+1:
            return
        if d==c_l+1:
            new_node=TreeNode(v)
            new_node.left=c_n.left
            c_n.left=new_node
            new_node=TreeNode(v)
            new_node.right=c_n.right
            c_n.right=new_node
        self.addUtil(c_n.left,c_l+1,d,v)
        self.addUtil(c_n.right,c_l+1,d,v)
        
