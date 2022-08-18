from ListNode import *


class Solution:
    def mergeTwoLists2(self, list1, list2):
        nodeit=ListNode()
        returnnode=nodeit
        while(list1!=None or list2!=None):
            minnode=None
            if(list1):
                minnode=list1
            if(list2):
                if(not list1 or list2.val<list1.val):
                    minnode=list2
            #print(minnode.val)
            nodeit.next=ListNode(minnode.val)
            nodeit=nodeit.next
            if(list1==minnode):
                list1=list1.next
            else:
                list2=list2.next
        return returnnode.next
    def mergeTwoLists(self, l1, l2):
        if(l1==None and l2!=None):
            return l2   
        elif(l1!=None and l2==None):
            return l1
        elif(l1==None and l2==None):
            return None
        if(l1.val<l2.val):
            newnode=ListNode(l1.val)
            l1=l1.next
        else:
            newnode=ListNode(l2.val)
            l2=l2.next
        tore=newnode
        while(True):
            if(l1==None and l2==None):
                break
            elif(l1==None):
                newnode.next=ListNode(l2.val)
                newnode=newnode.next
                l2=l2.next
            elif(l2==None):
                newnode.next=ListNode(l1.val)
                newnode=newnode.next
                l1=l1.next
            elif(l1.val>=l2.val):
                newnode.next=ListNode(l2.val)
                newnode=newnode.next
                l2=l2.next
            elif(l1.val<l2.val):
                newnode.next=ListNode(l1.val)
                newnode=newnode.next
                l1=l1.next
        return tore
                
    
s=Solution()
alist=createNode([1,2,4])
blist=createNode([1,3,4])
nodelist=s.mergeTwoLists2(alist,blist)
printNode(nodelist)


