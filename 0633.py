class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c+1):
            temp=i**2
            if(temp>c):
                break
            num=((c-temp)**0.5)
            if(num.is_integer()):
                return True
        return False
            
                    
            
                    
    

                

a=Solution()
print(a.judgeSquareSum(0))
