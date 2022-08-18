class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(singlestr,longstr):
            carry='0'
            final=''
            for i in longstr[::-1]:
                result=str(int(i)*int(singlestr)+int(carry))
                carry=result[0] if len(result)==2 else '0'
                final=result[1]+final if len(result)==2 else result[0]+final
            if(carry!='0'):final=carry+final
            return final
        def add(str1,str2):
            final=''
            carry='0'
            for ptr in range(1,max(len(str1),len(str2))+1):
                n1=str1[-ptr] if ptr<=len(str1) else '0'
                n2=str2[-ptr] if ptr<=len(str2) else '0'
                result=str(int(n1)+int(n2)+int(carry))
                carry=result[0] if len(result)==2 else '0'
                final=result[1]+final if len(result)==2 else result[0]+final
            if(carry!='0'):final=carry+final
            return final
        tore=''
        for i in range(1,len(num1)+1):
            temp=mul(num1[-i],num2)
            tore=add(temp+'0'*(i-1),tore)
        for i in range(len(tore)):
            if(tore[i]!='0' or i==len(tore)-1):
                return tore[i:]
            
                    
    

                

a=Solution()
print(a.multiply("0","456"))
