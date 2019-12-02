# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    def recover(self,root,elements,v=0):
        if not root:
            return
        if root.val==-1:
            elements[v]=True
        self.recover(root.left,elements,2*v+1)
        self.recover(root.right,elements,2*v+2)
        
    def __init__(self, root: TreeNode):
        self.root=root
        self.elements={}
        self.recover(self.root,self.elements)

    def find(self, target: int) -> bool:
        return target in self.elements        
