class Solution:
    # def ctotal(self):
    #     self.total=1
    # def numDecodings(self, s: str) -> int:
    #     table=[str(i) for i in range(1,27)]
    #     self.ctotal()
    #     def rec(s):
    #         if(len(s)==0):
    #             return
    #         if(s[0]=='0'):
    #             if(self.total>0):
    #                 self.total-=1   
    #         else:
    #             if(len(s)>=2):
    #                 if(s[:2] in table):
    #                     self.total+=1
    #                     rec(s[2:])
    #             rec(s[1:])
    #     rec(s)
    #     return self.total
    def numDecodings(self,s):
        table=[str(i) for i in range(1,27)]
        if(len(s)==1): #长度为1的情况
            if(s=='0'):return 0
            else:return 1
        if(len(s)==2): #长度为2的情况
            if(s in table):return 2
            else:return 1
        dp=[]
        meetnum=0
        for i in range(len(s)-1): #有连续0return0
            if(s[i]==0 and s[i+1]==0):
                return 0
        if(s[len(s)-1]=='0'):  #第一个dp
            if(s[len(s)-2]=='1' or s[len(s)-2]=='2'):
                meetnum=len(s)-2
                dp.append(s[len(s)-2:],1)
            else:
                return 0
        else:
            meetnum=len(s)-1
            dp.append(s[len(s)-1],1)
        istwo=0

                
                

            
                    

a=Solution()
# print(a.numDecodings("115231"))
# print(a.numDecodings("111111111111111111111111111111111111111111111"))
# print(a.numDecodings("0"))
print(a.numDecodings("29"))
