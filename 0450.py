# 删除一个BST中的元素
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
class Solution:
    def findNode(self,node,targetkey):
        if(node):
            if(node.val==targetkey):
                return [node,None,1,'']# 目标，父，层数，左右
            if(node.left):
                res=self.findNode(node.left,targetkey)
                if(res):
                    if(res[2]==1):
                        return [res[0],node,res[2]+1,'left']
                    else:
                        return [res[0],res[1],res[2]+1,res[3]]
            if(node.right):
                res=self.findNode(node.right,targetkey)
                if(res):
                    if(res[2]==1):
                        return [res[0],node,res[2]+1,'right']
                    else:
                        return [res[0],res[1],res[2]+1,res[3]]
            
    def presearch_first(self,node):
        if(node):
            if(node.left):
                res=self.presearch_first(node.left)
                if(res[2]==1):
                    return [res[0],node,res[2]+1]
                else:
                    return [res[0],res[1],res[2]+1]
            return [node,None,1]# 目标，父，层数
    
    def deleteNode(self, root, key: int):
        result1=self.findNode(root,key)
        if(not result1):
            return root
        targetNode,fatherNode,times,side=result1[0],result1[1],result1[2],result1[3]
        # 根节点就是要删除的节点
        if(times==1):
            resr=self.presearch_first(targetNode.right)
            if(not resr):
                return root.left
            if(resr[2]==1):
                # 根右边
                root.val=resr[0].val
                root.right=resr[0].right
            else:
                #移除原来的中序遍历第一个节点
                resr[1].left=resr[0].right
                root.val=resr[0].val
            return root
        #targetNode左无右无
        if(not targetNode.left and not targetNode.right):
            if(side=='left'):
                fatherNode.left=None
            else:
                fatherNode.right=None
        #targetNode左有右无
        if(targetNode.left and not targetNode.right):
            if(side=='left'):
                fatherNode.left=targetNode.left
            else:
                fatherNode.right=targetNode.left
        # targetNode左无右有
        if(not targetNode.left and targetNode.right):
            if(side=='left'):
                fatherNode.left=targetNode.right
            else:
                fatherNode.right=targetNode.right
        # 左有右有
        if(targetNode.left and targetNode.right):
            res=self.presearch_first(targetNode.right)
            if(res[2]==1):
                if(side=='left'):
                    fatherNode.left=res[0]
                    res[0].left=targetNode.left
                else:
                    fatherNode.right=res[0]
                    res[0].left=targetNode.left
            else:
                #移除原来的中序遍历第一个节点
                res[1].left=res[0].right
                targetNode.val=res[0].val
        return root
                    
        
nodetree=createTreeNode([5,3,6,2,4,None,7])
a=Solution()
printTreeNode_level(a.deleteNode(nodetree,3))