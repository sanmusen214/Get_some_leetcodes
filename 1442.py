class Solution:
    def countTriplets(self, arr) -> int:
        total=0
        for i in range(len(arr)-1):
            s=arr[i]
            for k in range(i+1,len(arr)):
                s^=arr[k]
                if(s==0):
                    total+=(k-i)
        return total
        

a=Solution()
print(a.countTriplets([2,3,1,6,7]))
