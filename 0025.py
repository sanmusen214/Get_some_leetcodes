from ListNode import *


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ret=head
        before=ListNode(-1)
        before.next=head
        tore=before
        while(True):
            storelist=[]
            if(whetherdone(ret,k)):
                break
            for i in range(k):
                storelist.append(ret)
                ret=ret.next
            before.next=storelist[len(storelist)-1]
            before=before.next
            temp=storelist[len(storelist)-1].next
            for i in range(len(storelist)-2,-1,-1):
                before.next=storelist[i]
                before=before.next
            before.next=temp
            
        return tore.next
def whetherdone(tnode,k):
    for i in range(k):
        if(tnode==None):
            return True
        tnode=tnode.next
    return False
                

                


                
            
a=Solution()
x=createNode([1,2,3,4,5])
y=createNode([1,3,4])
z=createNode([])
printNode(a.reverseKGroup(x,3))
