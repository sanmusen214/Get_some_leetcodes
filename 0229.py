class Solution:
    def majorityElement(self, nums: "List[int]") -> "List[int]":
        
        # pin=int(len(nums)/3)
        # table={}
        # for i in nums:
        #     if i not in table:
        #         table[i]=1
        #     else:
        #         table[i]+=1
        # res=[]
        # for k in table:
        #     if table[k]>pin:
        #         res.append(k)
        # return res
        
        # 摩尔投票法
        if(len(nums)==1):return nums
        army={}#维护两个阵营，遍历数，如果数和这两个阵营不同就厮杀
        for i in nums:
            if(i not in army):
                if(len(army.keys())<2):
                    army[i]=1
                else:
                    top=[]
                    for k in army:
                        army[k]-=1
                        if(army[k]==0):
                            top.append(k)
                    for p in top:
                        army.pop(p)
            else:
                army[i]+=1
        #验证人最多的两阵营人多于1/3
        return [each for each in list(army.keys()) if nums.count(each) >int(len(nums)/3)]
                    
a=Solution()
print(a.majorityElement([1,2,3]))

            