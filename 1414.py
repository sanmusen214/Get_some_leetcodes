class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        listf=[1,1]
        #创建适当长度的斐波拉契
        while(listf[-1]<=k):
            listf.append(listf[-1]+listf[-2])
        listf.pop(-1)
        def compute(nownumber,rightmost):
            if(nownumber>k):
                return -1
            if(nownumber==k):
                return 0
            for i in range(rightmost,-1,-1):
                nextLimp=compute(nownumber+listf[i],i)
                if(nextLimp>=0):
                    # print(listf[i],",",end=" ")
                    return nextLimp+1
        return compute(0,len(listf)-1)


a=Solution().findMinFibonacciNumbers(19)
print(a)