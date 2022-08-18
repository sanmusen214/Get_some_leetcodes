class Solution:
    def permutation(self, s: str):
        sets={}
        for i in s:
            if sets.get(i):
                sets[i]+=1
            else:
                sets[i]=1
        def cir(s,newsets):
            if(not newsets):
                outs.append(s)
                return
            for each in newsets:
                cha=each
                tempset=newsets.copy()
                if tempset[each]==1:
                    tempset.pop(each)
                else:
                    tempset[each]-=1
                cir(s+cha,tempset)
        outs=[]
        cir("",sets)
        return outs
                
                
                    
a=Solution()
print(a.permutation("abbccd"))


