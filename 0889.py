from TreeNode import *

class Solution:
    def constructFromPrePost(self, preorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        # preorder 范围prl,prr,
        # postorder 范围pol,por
        def build(prl,prr,pol,por):
            if(prl>prr or pol>por):
                return
            if(prl==prr and pol==por):
                return TreeNode(preorder[prl])
            print("preorder",preorder[prl:prr+1],"\npostorder",postorder[pol:por+1])
            # 确定左树根节点
            leftrootval=preorder[prl+1]
            # postorder左树长度
            ltree=0
            sppoind=0
            for i in range(pol,por+1):
                ltree+=1
                # postorder右树开头。左树，右树，中根
                if(postorder[i]==leftrootval):
                    sppoind=i+1
                    break
            # preorder右树开头。中根，左树，右树
            sppreind=prl+ltree+1
            return TreeNode(preorder[prl],build(prl+1,sppreind-1,pol,sppoind-1),build(sppreind,prr,sppoind,por-1))
        root=build(0,len(preorder)-1,0,len(postorder)-1)
        return root
a=Solution()
root=a.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])
printTreeNode_level(root)
