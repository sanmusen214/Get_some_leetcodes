from ListNode import *

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast=head
        slow=head
        while(1):
            if(fast == None):
                return None
            fast=fast.next


            if(fast == None):
                return None
            fast=fast.next
            slow=slow.next
            if(fast == slow):
                break  
        slow=head
        while(slow != fast):
            slow=slow.next
            fast=fast.next
        return slow
    
a=Solution()
listnodes=createNode([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
nnode=listnodes
for i in range(24):
    nnode=nnode.next
lnode=nnode
while(lnode and lnode.next):
    lnode=lnode.next
lnode.next=nnode
print(a.detectCycle(listnodes))