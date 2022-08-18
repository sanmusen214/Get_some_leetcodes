class Solution:
    def countAndSay(self, n: int) -> str:
        numlist=[]
        for i in range(n):
            if(i==0):
                numlist.append('1')
                continue
            countlist=[0,numlist[0]]
            for p in numlist:
                if(p==countlist[len(countlist)-1]):
                    countlist[len(countlist)-2]=str(int(countlist[len(countlist)-2])+1)
                if(p!=countlist[len(countlist)-1]):
                    countlist.append("1")
                    countlist.append(p)
            numlist= countlist
        return ''.join(numlist)
            
            
            
            





a=Solution()
print(a.countAndSay(5))
