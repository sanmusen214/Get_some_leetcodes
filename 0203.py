from ListNode import *


class Solution:
    def removeElements(self, head, val: int):
        if(head==None):
            return head
        while(1):#头节点
            if(head.val!=val):
                break
            else:
                head=head.next
                if(head==None):
                    break
        tnode=head
        while(1):#非头节点
            if(head==None):#尾节点next指针指向空的点退出
                break
            elif(head.next==None):#尾节点退出
                break
            elif(head.next.val==val):
                head.next=head.next.next#包括了对最后一个节点的检查
            else:
                head=head.next  
        return tnode
            
        
            
        
                
                    
a=Solution()
nodelist2=createNode([1,2,2,1])
printNode(a.removeElements(nodelist2,2))
