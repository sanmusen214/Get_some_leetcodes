import TreeNode
class Solution:
    def widthOfBinaryTree(self, root: 'Optional[TreeNode]') -> int:
        # 记录每一层的最左最右
        levels={}
        def findleft(root,level,ind):
            if(not root):
                return
            levels[level]=levels.get(level,[])+[ind]
            if(root.left):
                findleft(root.left,level+1,ind*2)
            if(root.right):
                findleft(root.right,level+1,ind*2+1)
        findleft(root,0,0)
        res=0
        for k in levels:
            res=max(res,levels[k][-1]-levels[k][0]+1)
        return res
        
a=Solution()
print(a.widthOfBinaryTree(TreeNode.createTreeNode([1,3,2,5,3,None,9,None,None,None,None,None,None])))
