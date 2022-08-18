class Solution:
    def reverse(self, x: int) -> int:
        mi=0
        if(x<0):
            x=-x
            mi=1
        numtemp=str(x)
        numlist=[]
        for i in range(len(numtemp)):
            numlist.append(numtemp[i])
        # print(numlist)
        for i in range(len(numlist)):
            if(i==int(len(numlist)/2)):
                break
            temp=numlist[i]
            numlist[i]=numlist[len(numlist)-1-i]
            numlist[len(numlist)-1-i]=temp
        # print(numlist)
        numstr=''
        for i in range(len(numlist)):
            numstr=numstr+numlist[i]
        # print(numstr)
        if(mi==0):
            num=float(numstr)
        else:
            num=float(numstr)*(-1)
        if(num>pow(2,31)-1 or num<-1*pow(2,31)):
            return 0
        else:
            return int(num)
                
                    
a=Solution()
print(a.reverse(-1234))#"PAHNAPLSIIGYIR"

