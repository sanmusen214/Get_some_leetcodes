# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        countdict=dict()
        def gen(left,right):
            if(left>right):
                return [TreeNode(-1)]
            if((left,right) in countdict):
                return countdict[(left,right)]
            tnodes=[]
            # 中心点
            for i in range(left,right+1):
                for ltree in gen(left,i-1):
                    if(ltree.val==-1):
                        ltree=None
                    for rtree in gen(i+1,right):
                        if(rtree.val==-1):
                            rtree=None
                        tnodes.append(TreeNode(i,ltree,rtree))
            countdict[(left,right)]=tnodes
            return tnodes
        
        return gen(1,n)
    
a=Solution()
print(a.generateTrees(3))