# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *


class Solution:
    minest=[]
    flag=0
    def findSecondMinimumValue(self, root) -> int:
        def pre(root):
            if(not root):return
            if(root.val<self.minest[0]):
                self.minest.pop(-1)
                self.minest.insert(0,root.val)
            elif(root.val>self.minest[0]):
                self.minest[1]=min(root.val,self.minest[1])
                self.flag=1
            pre(root.left)
            pre(root.right)
        self.minest=[float("inf")-1,float("inf")]
        self.flag=0
        pre(root)
        if(self.flag==0):return -1
        else:return self.minest[1]
a=Solution()
node=createTreeNode([3,3,3])
print(a.findSecondMinimumValue(node))
        