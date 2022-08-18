from ListNode import *
import math
class Solution:
    def splitListToParts(self, head, k: int):
        # 计算链表长度
        len_head=0
        temphead=head
        while(temphead):
            temphead=temphead.next
            len_head+=1
        
        # 开始截
        results=[]
        next_head=head
        # 总共截取k个子链
        while(k!=0):
            # 每次添加当前需求的平均数向上取整，下一次均分次数减一，被分的长度也减
            this_time_len=math.ceil(len_head/k)
            len_head-=this_time_len
            k-=1
            # 开始截取链表
            this_head=next_head
            results.append(this_head)
            # 往后截的次数
            for i in range(this_time_len-1):
                this_head=this_head.next
            # 如果没到链表末尾，则截断this_head.next
            if(this_head):
                next_head=this_head.next
                this_head.next=None
            # 到链表末尾则不用再次截断了
        return results
            
                
                
                    
a=Solution()
temptree=createNode([1,2,3])

ans=a.splitListToParts(temptree,5)
for each in ans:
    printNode(each)

