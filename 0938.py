from TreeNode import *


class Solution:
    def time(self):
        self.time=0
    def rangeSumBST(self, root, low: int, high: int) -> int:
        self.time()
        def BST(tree):
            if(tree.left!=None):
                BST(tree.left)
            if(tree.val<high and tree.val>=low):
                self.time+=tree.val
            if(tree.right!=None):
                BST(tree.right)
        BST(root)
        return self.time
            
            
                    
            
                    
    

                

a=Solution()
root1=createTreeNode([5,3,6,2,4,None,8,1,None,None,None,7,9])
print(a.rangeSumBST(root1,1,15))
