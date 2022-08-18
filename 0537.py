class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #解析
        s1=float(num1.split("+")[0])
        x1=float(num1.split("+")[1][:-1])
        s2=float(num2.split("+")[0])
        x2=float(num2.split("+")[1][:-1])
        print(s1," ",x1)
        print(s2," ",x2)
        
        #计算
        fs=s1*s2-x1*x2
        fx=s1*x2+x1*s2
        print(fs," ",fx)
        if(fs%1==0):
            fs=int(fs)
        if(fx%1==0):
            fx=int(fx)
        
        #字符串
        return str(fs)+"+"+str(fx)+"i"
        
        
            
            
                
                
a=Solution()
print(a.complexNumberMultiply("1+0i","1+0i"))
