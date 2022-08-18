class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #1 A
        #26 Z
        #27 AA
        #26=Z=A0
        total=0
        for i in range(len(columnTitle)-1,-1,-1):
            total+=((ord(columnTitle[i])-64)*(26**(len(columnTitle)-1-i)))
            print(ord(columnTitle[i])-64)
        return total
            
a=Solution()
print(a.titleToNumber("ABZ"))
print(a.titleToNumber("FXSHRXW"))
