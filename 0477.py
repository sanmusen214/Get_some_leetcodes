class Solution:
    def totalHammingDistance(self, nums):
        table=[0 for i in range(31)]
        for num in nums:
            t=str(bin(num))
            for b in range(-1,-len(t)+1,-1):
                if t[b]=='1':
                    table[b]+=1
        total=0
        for p in table:
            total+=p*(len(nums)-p)
        return total
        
a=Solution()
print(a.totalHammingDistance([9,7,3]))
                
            