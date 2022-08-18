class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations)):
            if(i+1>citations[i]):
                return i
            if(i+1==citations[i]):
                return i+1
        return len(citations)
a=Solution()
print(a.hIndex([1,3,1]))
print(a.hIndex([3,0,6,1,5]))
print(a.hIndex([1]))


            
        
                    

