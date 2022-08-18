# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    walkway={}
    station_num=0
    result=0
    #点之间的线代表前缀值，记录当前路径之前的前缀和，然后差分查找，采用字典存储，前缀和：出现次数
    def pathSum(self, root: "TreeNode", targetSum: int) -> int:
        self.result=0
        #这里0:1代表头节点与假象的首节点连线的值
        self.walkway={0:1}
        self.station_num=0
        def addonce(whichs):
            if(whichs in self.walkway):
                self.walkway[whichs]+=1
            else:
                self.walkway[whichs]=1
        def subonce(whichs):
            if(self.walkway[whichs]>1):
                self.walkway[whichs]-=1
            else:
                del self.walkway[whichs]
        def goahead(stand):
            #这次,先找再入集
            self.station_num+=stand.val
            if(self.station_num-targetSum in self.walkway):
                self.result+=self.walkway[self.station_num-targetSum]
            addonce(self.station_num)
            
            # print(self.walkway)
            #左右
            if(stand.left):
                goahead(stand.left)
            if(stand.right):
                goahead(stand.right)
            #取消这次
            subonce(self.station_num)
            self.station_num-=stand.val
        #输入为空
        if(not root):
            return 0
        goahead(root)
        return self.result
    
a=Solution()
tree1=createTreeNode([5,4,8,11,None,13,4,7,2,None,None,5,1])
tree2=createTreeNode([])
tree3=createTreeNode([0,0,None,None,None])
print(a.pathSum(tree1,22))

print(a.pathSum(tree2,2))

print(a.pathSum(tree3,0))