class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        checked=[0 for i in range(left,right+1)]
        for i in ranges:
            for index in range(i[0],i[1]+1):
                if(index>=left and index<=right):
                    checked[index-left]=1
        if(checked.count(0)==0):return True
        else: return False
a=Solution()
print(a.isCovered([[1,50]],1,50))