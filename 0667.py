class Solution:
    def constructArray(self, n: int, k: int):
        # [1,1+k,2,1+k-1,3,1+k-2...1+k/2]
        res=[]
        lastnum=None
        for i in range(1,n+1):
            if(i%2==1):   
                nownum=int((i+1)/2)
                if(i!=1 and nownum>=lastnum):
                    break
                res.append(nownum)
                lastnum=nownum
            else:
                nownum=k+2-int(i/2)
                if(nownum<=lastnum):
                    break
                res.append(nownum)
                lastnum=nownum
        # 从k+2开始等差1
        for i in range(k+2,n+1):
            res.append(i)
        return res

a=Solution()
print(a.constructArray(20,14))