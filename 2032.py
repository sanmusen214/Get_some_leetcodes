from ListNode import *


class Solution:
    #计算链表交叉长度，从该长度起点开始依次比对headA和B节点
    def getIntersectionNode(self, headA, headB):
        count1=0
        count2=0
        tA=headA
        tB=headB
        while(tA!=None):
            tA=tA.next
            count1+=1
        while(tB!=None):
            tB=tB.next
            count2+=1
        count1,count2=count1-min(count1,count2),count2-min(count1,count2)
        
        for i in range(count1):
            headA=headA.next
        for i in range(count2):
            headB=headB.next
    
        while(headA!=None):
            if(headA==headB):
                return headA
            headA=headA.next
            headB=headB.next
        return None
