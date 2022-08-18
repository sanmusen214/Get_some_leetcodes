class Solution:
    def isValid(self, s: str) -> bool:
        left=['(','{','[']
        right=[')','}',']']
        templist=[]
        for i in s:
            if(i in left):
                templist.append(i)
            else:
                if(len(templist)>=1 and i==right[left.index(templist[len(templist)-1])]):
                    del(templist[len(templist)-1])
                    continue
                else:
                    return False
        if(len(templist)==0):
            return True
        return False
        
            
a=Solution()
print(a.isValid(")"))
