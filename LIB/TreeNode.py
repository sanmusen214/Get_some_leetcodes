# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#循环创建二叉树
# def createTreeNode(numlist):
#     '''
#     use list to create digittree\n
#     leaf.left and leaf.right are None
#     '''
#     pstnum=1
#     first=TreeNode(numlist[0])
#     nextrow=[first]
#     while(1): 
#         treenode_list_row=nextrow
#         nextrow=[]
#         for pstrow in range(len(treenode_list_row)): #读上一行的父节点，依次再从numlist里取出两数字
#             if(pstnum==len(numlist)):
#                 break
#             if(numlist[pstnum]!=None): #数字为None就直接忽略填左子
#                 nextrow.append(TreeNode(numlist[pstnum])) #创建左子并append作为下次的父节点
#                 treenode_list_row[pstrow].left=nextrow[len(nextrow)-1] #赋值给父
#             pstnum+=1
#             if(pstnum==len(numlist)):
#                 break
#             if(numlist[pstnum]!=None): #数字为None就直接忽略填右子
#                 nextrow.append(TreeNode(numlist[pstnum])) #创建右子并append作为下次的父节点
#                 treenode_list_row[pstrow].right=nextrow[len(nextrow)-1]
#             pstnum+=1
#         if(pstnum==len(numlist)):
#             break
#     return first



#递归循环创建二叉树 保留树每行的非None的nodes递归
def createtree(numlist,nodelist):
    numptr=0
    newnodelist=[]
    for nodeptr in range(len(nodelist)):
        if(numlist[numptr]!=None):
            temp=TreeNode(numlist[numptr])
            nodelist[nodeptr].left=temp
            newnodelist.append(temp)
        numptr+=1
        if(numptr>=len(numlist)):break
        if(numlist[numptr]!=None):
            temp=TreeNode(numlist[numptr])
            nodelist[nodeptr].right=temp
            newnodelist.append(temp)
        numptr+=1
        if(numptr>=len(numlist)):break
    if(len(numlist)<=2*len(nodelist)):
        return
    createtree(numlist[2*len(nodelist):],newnodelist)
    
def createTreeNode(numlist):
    if not numlist:
        return None
    firstnode=TreeNode(numlist[0])
    createtree(numlist[1:],[firstnode])
    return firstnode
#* 也可以用满二叉树输入然后用定位下标的方式DFS生成二叉树

def printTreeNode_pre(headnode):
    '''
    前序遍历
    '''
    if(headnode==None):
        # print(None,end=" ")
        return
    print(headnode.val,end=" ")
    printTreeNode_pre(headnode.left)
    printTreeNode_pre(headnode.right)
    
def printTreeNode_in(headnode):
    '''
    中序遍历
    '''
    if(headnode==None):
        # print(None,end=" ")
        return
    printTreeNode_in(headnode.left)
    print(headnode.val,end=" ")
    printTreeNode_in(headnode.right)

def printTreeNode_post(headnode):
    '''
    后序遍历
    '''
    if(headnode==None):
        # print(None,end=" ")
        return
    printTreeNode_post(headnode.left)
    printTreeNode_post(headnode.right)
    print(headnode.val,end=" ")
    
def printTreeNode_level(headnode):
    '''
    层序遍历
    '''
    treelist=[headnode]                                             #treelist会按层存储树的所有节点
    p=0                                                             #指针指向当前第一个根节点
    while(p<len(treelist)):                                         #指针超过list总长就退出循环
        if(treelist[p]=='None'):
            print('None',end=' ')
            p+=1
            continue
        print(treelist[p].val,end=" ")     
        if(treelist[p].left):
            treelist.append(treelist[p].left)      #如果有左儿子，左儿子加入list
        else:
            treelist.append('None')
        if(treelist[p].right):
            treelist.append(treelist[p].right)    #如果有右儿子，右儿子加入list
        else:
            treelist.append('None')
        p+=1                                                        #指针后移，指向同层下一节点或下层第一个节点
            
    

if __name__=='__main__':   
    listnode=createTreeNode([6,1,7,None,4,None,10,3,None,9,None,None,None,8,None,None,None])
    print("pre")
    printTreeNode_pre(listnode)
    print("\nin")
    printTreeNode_in(listnode)
    print("\npost")
    printTreeNode_post(listnode)
    print("\nlevel")
    printTreeNode_level(listnode)
    # a=TreeNode()
    # a.left=TreeNode()
    # print(a.left == TreeNode())
