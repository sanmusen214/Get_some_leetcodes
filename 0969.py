class Solution:
    def pancakeSort(self, arr: "List[int]") -> "List[int]":
        result=[]
        #将ind位置的东西先翻转到第一，然后翻转到towhere
        #实现为将ind之后的翻转放到ind之前
        def takeAhead(ind,towhere):
            result.extend([ind+1,towhere+1])
            rightList=arr[ind+1:towhere+1]
            rightList.reverse()
            return rightList+arr[:ind+1]+arr[towhere+1:]
        #找到数组内end之前（包括end 最大的东西的下标
        def findMaxitem(end):
            ptr=0
            #下标，数
            mpair=[float("-inf"),float("-inf")]
            while(ptr<=end):
                if(arr[ptr]>mpair[1]):
                    mpair=[ptr,arr[ptr]]
                ptr+=1
            return mpair[0]
        for i in range(len(arr)-1,-1,-1):
            cdx=findMaxitem(i)
            arr=takeAhead(cdx,i)
        print(arr)
        return result
            
        
            
a=Solution()

nums=[4,5,7,6,2]
print(a.pancakeSort(nums))
