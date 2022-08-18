class Solution:
    def findneareast(self,nlist,target):
        ll=0
        rr=len(nlist)-1
        least=float("inf")
        while(1):
            cc=int((ll+rr)/2)
            if(ll>=rr):
                break
            least=min(least,abs(nlist[cc]-target))
            if(nlist[cc]>target):
                rr=cc
            elif(nlist[cc]<target):
                ll=cc
            elif(nlist[cc]==target):
                least=0
                break
        return least

    def minAbsoluteSumDiff(self, nums1, nums2):
        # 找到nums2对应的nums1每一个数字被替换后最多可以比原先配对缩小多少
        diff=[abs(nums2[i]-nums1[i]) for i in range(len(nums1))]
        sortnums1=nums1[::]
        sortnums1.sort()
        # 存放被替换后最多比当前差缩小多少
        tran_diff_nums=[]
        for i in range(len(nums2)):
            fixdiff=abs(nums2[i]-nums1[i])
            bestfit=self.findneareast(sortnums1,nums2[i])  
            print("for num:" ,nums2[i],"bestfit is:",bestfit)
            tran_diff_nums.append(bestfit-fixdiff)
        # print(diff)
        # print(tran_diff_nums)
        return (sum(diff)+min(tran_diff_nums))%(10**9+7)

                
                
                
                    
                
                
                

a=Solution()
# print(a.minAbsoluteSumDiff([1,10,4,4,2,7],
#                            [9,3,5,1,7,4])) #20
# print(a.minAbsoluteSumDiff([1,28,21],
#                            [9,21,20])) #9 [8,0,1]
#6717234
print(a.minAbsoluteSumDiff([150,100],
                            [90,10]))
