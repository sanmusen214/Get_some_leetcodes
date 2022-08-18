class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for p in range(len(nums)-1,-1,-1):
            if(whether_biggest(nums[p:])):
                continue
            else:
                target=choose_sec_bigger(nums[p:])
                sec_big_num=nums.pop(p+target)
                nums.insert(p,sec_big_num)
                sort_part=nums[p+1:]
                sort_part.sort()
                for i in range(len(sort_part)):
                    nums[p+1+i]=sort_part[i]
                return
        nums.reverse()
                
                
    
def whether_biggest(numlist):
    for i in range(len(numlist)-1):
        if(numlist[i]!=max(numlist[i:])):
            return False
    return True
            
def choose_sec_bigger(numlist):#比第一个稍大的下标
    colist=numlist.copy()
    biggest=numlist[0]
    for i in range(len(numlist)-1,-1,-1):
        if(numlist[i]<=biggest):
            numlist.pop(i)
    return colist.index(min(numlist))

        
        
        
            
            
a=Solution()

numlist1=[1,3,2]
a.nextPermutation(numlist1)#2,1,3
print(numlist1)

numlist2=[2,3,1]
a.nextPermutation(numlist2)#3,1,2
print(numlist2)

numlist3=[3,2,1]
a.nextPermutation(numlist3)#1,2,3
print(numlist3)

numlist4=[5,4,7,5,3,2]
a.nextPermutation(numlist4)#[5,5,2,3,4,7]
print(numlist4)

numlist5=[4,2,0,2,3,2,0]
a.nextPermutation(numlist5)#[4,2,0,3,0,2,2]
print(numlist5)
