# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        rootrow=[root]
        tl=[]
        while(rootrow.count(None)!=len(rootrow)):
            newrow=[]
            for i in rootrow:
                if(i!=None):
                    tl.append(i.val)
                    newrow.append(i.left)
                    newrow.append(i.right)
                else:
                    tl.append(None)
                    newrow.append(None)
                    newrow.append(None)
            rootrow=newrow
        m=tl.index(x)
        n=tl.index(y)
        if(m>n):
            m,n=n,m
        if(abs(m-n)==1 and m%2!=0):
            return False
        def whichlevel(num):
            if(num==0):
                return 0
            level=0
            while(pow(2,level)-2<num):
                level+=1
            return level-1
        mlevel=whichlevel(m)
        nlevel=whichlevel(n)
        if(mlevel!=nlevel):
            return False
        else:
            return True
                
            
        
a=Solution()
r=createTreeNode([1,2,3,None,4,None,5])
print(a.isCousins(r,5,4))#T
r2=createTreeNode([10,1,2,3,4,5,6])
print(a.isCousins(r2,5,4))#T