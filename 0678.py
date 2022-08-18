class Solution:
    def checkValidString(self, s: str) -> bool:
        prelist=[]
        left=0
        star=0
        def inthis(listm,target):
            for i in range(len(listm)-1,-1,-1):
                if(listm[i]==target):
                    return i
            return -1
        # 去掉所有右括号，右括号先与左括号匹配，再与星号匹配。
        for i in s:
            prelist.append(i)
            if(i=="("):
                left+=1
            if(i=="*"):
                star+=1
            if(i==")"):
                if(left>=1):
                    a=inthis(prelist,"(")
                    prelist.pop(a)
                    left-=1
                else:
                    if(star>=1):
                        b=inthis(prelist,"*")
                        prelist.pop(b)
                        star-=1
                    else:
                        return False
        #solute prelist
        # 当左侧有(号时，要确保右侧的)足够多，所以从右往左遍历
        cstar=0
        for i in range(len(prelist)-1,-1,-1):
            if(prelist[i]=="*"):
                cstar+=1
            if(prelist[i]=="("):
                cstar-=1
                if(cstar<0):
                    return False
            # if()
        return True
    
a=Solution()
print(a.checkValidString("(((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)"))