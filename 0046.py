class Solution:
    def permute(self, nums):
        def dfs(pre,last):
            if(len(last)==1):
                relist.append(pre+last)
            for i in range(len(last)):
                dfs(pre+[last[i]],last[:i]+last[i+1:])
        relist=[]
        dfs([],nums)
        return relist
            
    

                

a=Solution()
print(a.permute([1,2,3]))
