from TreeNode import *


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def pt(root,listm):
            if(root.left==None and root.right==None):
                listm.append(root.val)
            if(root.left!=None):pt(root.left,listm)
            if(root.right!=None):pt(root.right,listm)
            return listm
        list1=pt(root1,[])
        list2=pt(root2,[])    
        return list1==list2

tree1=createTreeNode([1,2,3])
tree2=createTreeNode([1,3,2])
a=Solution()
print(a.leafSimilar(tree1,tree2))
