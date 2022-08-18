class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=0,0,1
        for i in range(n+1):
            a,b,c=b,c,a+b+c
        return a
                
a=Solution()
print(a.tribonacci(56))
