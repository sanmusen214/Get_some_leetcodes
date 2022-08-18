import re
class Solution:
    def decodeString(self, s: str) -> str:
        self.stack=[]
        self.brackets=dict()
        # 括号匹配
        for i in range(len(s)):
            if(s[i]=='['):
                self.stack.append(i)
            elif(s[i]==']'):
                self.brackets[self.stack.pop()]=i
        # 递归解析[]中内容
        def decodeOne(start,end):
            numstart=-1# 第一个数字
            ptr=start
            res=""
            while(ptr<=end):
                if(s[ptr].isdigit() and numstart==-1):
                    numstart=ptr
                elif(s[ptr]=='[' and numstart!=-1):# '['
                    # 处理递归
                    res+=int(s[numstart:ptr])*decodeOne(ptr+1,self.brackets[ptr]-1)
                    # 指针跳过递归内容
                    ptr=self.brackets[ptr]
                    # 重新寻找下一个数字
                    numstart=-1
                elif(numstart==-1):
                    res+=s[ptr]
                ptr+=1
            return res
        return decodeOne(0,len(s)-1)
    
a=Solution()
print(a.decodeString("3[a12[c]]"))