class Solution:
    def islegal(self,hh,mm):
        if(int(hh)>=0 and int(hh)<=23 and int(mm)>=0 and int(mm)<=59):
            return True
        return False
    def maximumTime(self, time: str) -> str:
        tlist=[i for i in time]
        tlist.remove(":")
        unknown=[]
        for i in range(len(tlist)):
            if(tlist[i]=="?"):
                tlist[i]="0"
                unknown.append(i)
        for i in range(len(tlist)):
            if(i in unknown):
                for num in range(9,0,-1):
                    tlist[i]=str(num)
                    if(self.islegal(tlist[0]+tlist[1],tlist[2]+tlist[3])):
                        break
        tlist.insert(2,":")
        return "".join(tlist)

a=Solution()
print(a.maximumTime("??:??"))
