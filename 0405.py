class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num=num+2**32
        results=[""]
        while(num>0):
            t=num%16
            if(t<10):
                results.append(str(t))
            else:
                results.append(chr(t+87))
            num=int(num/16)
        return "".join(reversed(results))

a=Solution()
print(a.toHex(26))
