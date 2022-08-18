# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.state=0
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if(root and root.left):
            a=self.inorderSuccessor(root.left,p)
            if(a):return a
        if(root==p and self.state==0):
            self.state=1
        elif(self.state==1):
            return root
        if(root and root.right):
            c=self.inorderSuccessor(root.right,p)
            if(c):return c
        return False
        
