class Solution:
    def distributeCandies(self, candyType) -> int:
        half=len(candyType)/2
        types=set()
        count=0
        for c in candyType:
            if c not in types:
                count+=1
                types.add(c)
                if(count==half):
                    break
        return count
    
    
a=Solution()
print(a.distributeCandies([1,1,2,3]))