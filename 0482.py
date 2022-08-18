class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newstr=[""]
        count=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=="-"):
                continue
            else:
                p=s[i]
                if('a'<=p<='z'):
                    p=chr(ord(p)-32)
                newstr.append(p)
                count+=1
                if(count==k):
                    newstr.append('-')
                    count=0
        if(newstr[-1]=="-"):newstr.pop(-1)
        return "".join(reversed(newstr))
        
        
a=Solution()
print(a.licenseKeyFormatting("---",3))
