from TreeNode import *


class Solution:
    ref={}
    def verticalTraversal(self, root):
        self.ref={}
        def level(headnode):
            headnode.val=[0,0,headnode.val]
            treelist=[headnode]
            p=0
            while(p<len(treelist)):
                if(treelist[p].val[0] in self.ref):
                    if(treelist[p].val[1] in self.ref[treelist[p].val[0]]):
                        self.ref[treelist[p].val[0]][treelist[p].val[1]].append(treelist[p].val[2])
                    else:
                        self.ref[treelist[p].val[0]][treelist[p].val[1]]=[treelist[p].val[2]]
                else:
                    self.ref[treelist[p].val[0]]={treelist[p].val[1]:[treelist[p].val[2]]}
                if(treelist[p].left):
                    treelist[p].left.val=[treelist[p].val[0]-1,treelist[p].val[1]+1,treelist[p].left.val]
                    treelist.append(treelist[p].left)
                if(treelist[p].right):
                    treelist[p].right.val=[treelist[p].val[0]+1,treelist[p].val[1]+1,treelist[p].right.val]
                    treelist.append(treelist[p].right)
                p+=1
        level(root)
        ks=sorted(list(self.ref.keys()))
        results=[]
        for k in ks:
            small=[]
            for sk in self.ref[k]:
                if(len(self.ref[k][sk])==1):
                    small.append(self.ref[k][sk][0])
                else:
                    for inum in sorted(self.ref[k][sk]):
                        small.append(inum)
            results.append(small)
        return results
a=Solution()
tree=createTreeNode([3,1,4,0,2,2])
print(a.verticalTraversal(tree))
