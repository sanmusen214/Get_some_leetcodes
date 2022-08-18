class Solution:
    def isUgly(self, n: int) -> bool:
        if(n<=0):
            return False
        while(1):
            if(n%2!=0 and n%3!=0 and n%5!=0):
                break
            if(n!=0 and n%2==0):
                n/=2
            if(n!=0 and n%3==0):
                n/=3
            if(n!=0 and n%5==0):
                n/=5
        if(n==0 or n==1):
            return True
        else:
            return False
m=Solution()
print(m.isUgly(0))
