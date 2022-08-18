import random
nums=[5,5,5,3,2,4,8,7,6,9,4,8,4,1,3,6,5,7,9,2,6,8,0,1,2,6,2,5,7,9]
#把<锚点的放到锚点左边，指针必不会触右端
def quicksort(start,end):
    if(end-start<=1):return nums
    ff=random.randint(start,end-1)
    flagnum=nums[ff]
    #把锚点放到最左边
    nums[ff],nums[start]=nums[start],nums[ff]
    lptr=start
    for i in range(start,end):
        if(nums[i]<flagnum):
            nums[i],nums[lptr]=nums[lptr],nums[i]
            lptr+=1
    if(lptr==start):
        lptr+=1
    quicksort(start,lptr)
    quicksort(lptr,end)
    return nums
#把<=锚点的放到锚点左边，指针必会右移至少1
def quicksort2(start,end):
    if(end-start<=1):return nums
    ff=random.randint(start,end-1)
    #把锚点放到最右边
    nums[ff],nums[end-1]=nums[end-1],nums[ff]
    lptr=start
    for i in range(start,end):
        if(nums[i]<=nums[end-1]):
            nums[i],nums[lptr]=nums[lptr],nums[i]
            lptr+=1
    if(lptr==end):
        lptr-=1
    quicksort2(start,lptr)
    quicksort2(lptr,end)
    return nums
print(quicksort(0,len(nums)))