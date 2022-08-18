class Solution:
    def letterCombinations(self, digits: str):
        global strlist
        strlist=[]
        global reflist
        reflist=[['a','b','c'],
                ['d','e','f'],
                ['g','h','i'],
                ['j','k','l'],
                ['m','n','o'],
                ['p','q','r','s'],
                ['t','u','v'],
                ['w','x','y','z']]
        digits=digits+' '
        countcomb('',digits)
        return strlist
        
def countcomb(lstrs,rstrs):
    if(len(rstrs)==1):
        strlist.append(lstrs)
    else:
        for i in range(len(reflist[int(rstrs[0])-2])):
            countcomb(lstrs+reflist[int(rstrs[0])-2][i],rstrs[1:])
    


s=Solution()
print(s.letterCombinations("23"))
