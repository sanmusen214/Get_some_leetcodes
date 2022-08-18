class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        times=1
        while(times*2*k<=len(s)):
            tl=s[(times-1)*2*k:times*2*k-k]
            print(tl)
            tl.reverse()
            s[(times-1)*2*k:times*2*k-k]=tl
            times+=1
        times-=1
        if(len(s)-times*2*k<k):
            tl=s[times*2*k:]
            tl.reverse()
            s[times*2*k:]=tl
        else:
            tl=s[times*2*k:times*2*k+k]
            tl.reverse()
            s[times*2*k:times*2*k+k]=tl
        return "".join(s)
            
    
a=Solution()
print(a.reverseStr("abcdefg",2))