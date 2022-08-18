class Solution:
    def checkRecord(self, s: str) -> bool:
        counta=0
        countl=0
        startl=False
        for i in s:
            if(i=="A"):
                counta+=1
                if(counta==2):
                    return False
            if(i=="L"):
                countl+=1
                if(countl==3):
                    return False
            if(i!="L"):
                countl=0
        return True
a=Solution()
print(a.checkRecord("LALL"))

            