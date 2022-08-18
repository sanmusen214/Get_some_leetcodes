from TreeNode import *


def add_to_list_by_row(node,nodelist_val):
    if(node==None):
        return
    nodelist_val.append(node.val) #中序遍历
    add_to_list_by_row(node.left,nodelist_val)
    add_to_list_by_row(node.right,nodelist_val)
class Solution:
    def minDiffInBST(self, root) -> int:
        val=[]
        add_to_list_by_row(root,val)
        minnum=float("inf")
        for i in range(len(val)):
            if(val[i]==None):
                continue
            for j in range(i+1,len(val)):
                if(val[j]==None):
                    continue
                if(abs(val[i]-val[j])<minnum):
                    minnum=abs(val[i]-val[j])
        
        return minnum







s=createTreeNode([1,7,35,None,None,12,49])
a=Solution()
print(a.minDiffInBST(s))
