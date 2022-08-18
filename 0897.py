from TreeNode import *


class Solution:
    def time(self):
        self.time=0
    def retree(self):
        self.retree=TreeNode(0)
    def increasingBST(self, root):
        self.time()
        self.retree()
        potree=self.retree
        def BST(tree):
            if(tree.left!=None):
                print("jump left")
                BST(tree.left)
            elif(tree.left==None):
                print("add node left None")
                self.retree.left=None
            if(self.time==0):
                print("create fst node",tree.val)
                self.retree.val=tree.val
                self.time=1
            elif(self.time==1):
                print("add node",tree.val)
                self.retree.right=TreeNode(tree.val)
                self.retree=self.retree.right
            if(tree.right!=None):
                print("jump right")
                BST(tree.right)
            elif(tree.right==None):
                print("add node left None")
                self.retree.left=None
        BST(root)
        return potree
            
            
                    
            
                    
    

                

a=Solution()
root1=createTreeNode([5,3,6,2,4,None,8,1,None,None,None,7,9])
fr1=a.increasingBST(root1)
printTreeNode_in(root1)
