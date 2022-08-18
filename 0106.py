from TreeNode import *
class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        # inorder 范围il,ir,
        # postorder 范围pl,pr
        def build(il,ir,pl,pr):
            if(il>ir or pl>pr):
                return
            print("inorder",inorder[il:ir+1],"\npostorder",postorder[pl:pr+1])
            # 确定根节点
            rootval=postorder[pr]
            # inorder左树长度
            ltree=0
            spinind=0
            for i in range(il,ir+1):
                ltree+=1
                # inorder中根。左树，中根，右树
                if(inorder[i]==rootval):
                    ltree-=1#中根不算左树长度
                    spinind=i
                    break
            # postorder右树开头。左树，右树，中根
            sppostind=pl+ltree
            return TreeNode(rootval,build(il,spinind-1,pl,sppostind-1),build(spinind+1,ir,sppostind,pr-1))
        root=build(0,len(inorder)-1,0,len(postorder)-1)
        return root
    
a=Solution()
root=a.buildTree([9,3,15,20,7],[9,15,7,20,3])
printTreeNode_level(root)