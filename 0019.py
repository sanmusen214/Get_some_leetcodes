from ListNode import *  # import Listcode的话在使用其类方法时需要声明是Listcoe后的方法


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if(head.next==None and n==1):
            return None
        target=head
        tru=1
        length=0
        while(tru):
            if(head==None):
                break
            head=head.next
            length+=1
        head=target
        ptr=length-n
        if(ptr==0):
            return target.next
        for i in range(ptr-1):
            head=head.next
        store=head.next
        head.next=store.next
        return target
    
    
s=Solution()
nodelist=createNode([1,2])
printNode(s.removeNthFromEnd(nodelist,2))
nodelist2=createNode([1,2,3,4,5])
printNode(s.removeNthFromEnd(nodelist2,2))


