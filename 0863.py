from TreeNode import *


class Solution:
    def distanceK(self, root, target, k: int):
        graphs={}#存储图
        treelist=[root]
        p=0
        graphs[root]=[]
        while(p<len(treelist)):
            if(treelist[p].left):
                graphs[treelist[p]].append(treelist[p].left)
                graphs[treelist[p].left]=[treelist[p]]
                treelist.append(treelist[p].left)
            if(treelist[p].right):
                graphs[treelist[p]].append(treelist[p].right)
                treelist.append(treelist[p].right)
                graphs[treelist[p].right]=[treelist[p]]
            p+=1
        #* test
        # for each in graphs:
        #     print(each.val,":",end="")
        #     for v in graphs[each]:
        #         print(v.val,end=",")
        #     print()
        # 寻找距离target为k的所有节点,BFS
        result=[]
        finding=[target]
        found=[target]
        times=0
        while(finding and times!=k):
            newfinding=[]
            #根据上一轮检测的节点
            for nownode in finding:
                #检测下一个节点是否已见过
                for nextnode in graphs[nownode]:
                    if(nextnode not in found):
                        #添加到下一轮需要遍历的列表和已见过的列表
                        newfinding.append(nextnode)
                        found.append(nextnode)
            finding=newfinding
            times+=1
        return [n.val for n in finding]
a=Solution()
datatree=createTreeNode([3,5,1,6,2,0,8,None,None,7,4])
target=datatree.left
result=a.distanceK(datatree,target,2)
print(result)
