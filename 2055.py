
class Solution:
    def platesBetweenCandles(self, s: str, queries):
        #前缀和
        presum={}#记录[前缀和，前一个蜡烛下标，下一个蜡烛下标],盘子的话前缀和为-1
        #前后,记录前缀和和盘子的前一个蜡烛下标
        sum=0
        lastcheck=-1
        len_s=len(s)
        for i in range(len(s)):
            if(s[i]=="*"):
                sum+=1
                presum[i]=[-1,lastcheck,len_s]
            else:
                presum[i]=[sum,i,i]
                lastcheck=i
        #后前，记录盘子的下一个蜡烛下标
        lastcheck=len_s
        for i in range(len(s)-1,-1,-1):
            if(s[i]=="*"):
                presum[i][2]=lastcheck
            else:
                lastcheck=i
        # print(presum)
        #查询
        result=[]
        for each in queries:
            start=each[0]
            end=each[1]
            info_start=presum[start]
            info_end=presum[end]
            if info_start[0]!=-1:
                startsum=info_start[0]
            else:
                if(info_start[2]>end):
                    result.append(0)
                    continue
                startsum=presum[info_start[2]][0]
            if info_end[0]!=-1:
                endsum=info_end[0]
            else:
                if(info_end[1]<start):
                    result.append(0)
                    continue
                endsum=presum[info_end[1]][0]
            result.append(endsum-startsum)
        return result
        
                

a=Solution()
print(a.platesBetweenCandles("||*",[[2,2]]))

