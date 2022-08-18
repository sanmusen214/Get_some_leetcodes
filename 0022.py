class Solution:
    def generateParenthesis(self, n: int):
        strlist=[]
        def create(pstr):
            if(len(pstr)==2*n):
                if(not pstr in strlist):
                    strlist.append(pstr)
                return
            for i in range(len(pstr)):
                create(pstr[:i]+"()"+pstr[i:])
        create("()")
        return strlist
    
            
a=Solution()
print(a.generateParenthesis(3))
