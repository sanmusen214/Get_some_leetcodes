class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip(' ')
        if(s[0]=='-'):
            val=0
            s=s[1:]
        else:
            val=1
        if(not s[0].isdigit()):
            return 0
        ptr=len(s)
        for i in range(len(s)):
            if(not s[i].isdigit()):
                ptr=i
                break
        num=float(s[:ptr])
        if num>pow(2,31)-1:
            return pow(2,31)-1
        if num<-pow(2,31):
            return -pow(2,31)
        return pow(-1,val+1)*int(num)
                
                    
a=Solution()
print(a.myAtoi(" -48"))

