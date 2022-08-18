class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        # 记录目前为止的总和
        totallist=[0]
        total=0
        for i in nums:
            total+=i
            totallist.append(total)
        print(totallist)
        count=0
        # 哈希表记录所有右值，遍历totallist作为右值，从哈希表中查询要想得到goal的差，其左值有多少个
        # hashmap起始值为0:1，代表最左边的边界（下标0）
        hashmap={0:1}
        for i in range(1,len(totallist)):
            r=totallist[i]
            l=r-goal
            count=count+hashmap[l] if l in hashmap else count
            hashmap[r]=hashmap[r]+1 if r in hashmap else 1
        return count
                
        
        
        
            
                
                
    
a=Solution()
print(a.numSubarraysWithSum([1,0,1,0,1],2))#4
print(a.numSubarraysWithSum([0,0,0,0,0],0))#15
print(a.numSubarraysWithSum([0,0,0,0,0,0,1,0,0,0],0))#27
            