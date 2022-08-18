class Solution:
    def simplifiedFractions(self, n: int) -> "List[str]":
        nummap={1:{1}}
        for num in range(1,n+1):
            for prenum in range(2,num):
                if(num%prenum==0):
                    temp=nummap[prenum].copy()
                    temp=temp|nummap[int(num/prenum)]
                    nummap[num]=temp
                    break
            if(num not in nummap):
                nummap[num]={num}
                
        result=[]
        def comparesame(a,b):
            for each in a:
                if each in b:
                    return True
            return False
        
        for son in range(1,n):
            for mother in range(son+1,n+1):
                if(not comparesame(nummap[mother],nummap[son])):
                    result.append(str(son)+"/"+str(mother))
        print(nummap)
        return result
    
a=Solution()
print(a.simplifiedFractions(2))
print(a.simplifiedFractions(12))
print(a.simplifiedFractions(4))
