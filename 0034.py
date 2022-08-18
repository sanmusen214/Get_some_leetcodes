class Solution:
    def searchRange(self, nums, target):
        def binsearch(ll,rr,type=0):
            while(rr-ll>1):
                # print(ll,rr,type)
                cc=int((ll+rr)/2)
                if(nums[cc]==target):
                    if(type==-1):
                        return binsearch(ll,cc,-1)
                    elif(type==1):
                        return binsearch(cc,rr,1)
                    return [min(binsearch(ll,cc,-1)),max(binsearch(cc,rr,1))]
                if(nums[cc]>target):
                    rr=cc
                else:
                    ll=cc
            if(type==-1):
                return [rr,rr]
            if(type==1):
                return [ll,ll]
            return [-1,-1]
        return binsearch(-1,len(nums))
            
            
            

a=Solution()
print(a.searchRange([1],1))

