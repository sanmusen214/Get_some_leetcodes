from ListNode import *


class Solution:
    def swapPairs(self, head) -> ListNode:
        ret=head
        bef=ListNode(-1)
        bef.next=head
        tore=bef
        while(True):
            if(ret==None or ret.next==None):
                break
            bef.next=ret.next
            temp=ret.next.next
            ret.next.next=ret
            ret.next=temp
            bef=ret
            ret=ret.next
        return tore.next
                
                
                


                
            
a=Solution()
x=createNode([1,2,3,4,5])
y=createNode([1,3,4])
z=createNode([])
printNode(a.swapPairs(x))
