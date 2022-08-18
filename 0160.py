from ListNode import *
class Solution:
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
                return headA.val
            headA=headA.next
            headB=headB.next
        return None
        
            
        
                
                    
a=Solution()
nodelist1=createNode([4,1,8,4,5])
nodelist2=createNode([5,0,1,8,4,5])
print(a.getIntersectionNode(nodelist1,nodelist2))
