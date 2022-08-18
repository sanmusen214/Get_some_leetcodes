from ListNode import *


class Solution:
    def mergeKLists(self, lists):
        time=1
        rtnode=None
        i=0
        while(lists):
            if(lists==[]):
                break
            if(time==1):
                nodels=[]
                while(time==1):
                    if(i==len(lists)):
                        break
                    elif(lists[i]!=None):
                        v=int(lists[i].val)
                        nodels.append(v)
                        i+=1
                    else:
                        lists.pop(i)
                time=2
                continue
            if(time==2):
                rtnode=renode=ListNode(min(nodels))
                time=3
            else:
                renode.next=ListNode(min(nodels))
                renode=renode.next
            dex=nodels.index(min(nodels))
            lists[dex]=lists[dex].next
            if(lists[dex]==None):
                lists.pop(dex)
                nodels.pop(dex)
            else:
                nodels[dex]=lists[dex].val
        return rtnode
            
a=Solution()
x=createNode([1,4,5])
y=createNode([1,3,4])
z=createNode([])
printNode(a.mergeKLists([x,y,z]))
