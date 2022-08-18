from TreeNode import *
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        # preorder 范围pl,pr,
        # inorder 范围il,ir
        def build(pl,pr,il,ir):

            if(pl>pr or il>ir):
                return
            # print("preorder",preorder[pl:pr+1],"\ninorder",inorder[il:ir+1])
            # 确定根节点
            rootval=preorder[pl]
            # inorder左树长度
            ltree=0
            spinind=0
            for i in range(il,ir+1):
                ltree+=1
                # inorder中根。左树，中根，右树
                if(inorder[i]==rootval):
                    spinind=i
                    break
            # preorder右树开头。中根，左树，右树
            sppreind=pl+ltree
            return TreeNode(rootval,build(pl+1,sppreind-1,il,spinind-1),build(sppreind,pr,spinind+1,ir))
        root=build(0,len(preorder)-1,0,len(inorder)-1)
        return root
    
a=Solution()
root=a.buildTree([3,9,20,15,7],[9,3,15,20,7])
printTreeNode_level(root)