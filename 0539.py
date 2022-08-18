class Solution:
    def findMinDifference(self, timePoints: "List[str]") -> int:
        def insertL(listm,newnum):
            l=-1
            r=len(listm)
            c=int((l+r)/2)
            while(1):
                c=int((l+r)/2)
                print(l," ",c," ",r)
                if(c==l or c==r):
                    return r
                elif(newnum>listm[c]):
                    l=c
                elif(newnum<listm[c]):
                    r=c
                else:
                    return -1
        timelist=[int(timePoints[0][:2])*60+int(timePoints[0][3:])]
        for tp in range(1,len(timePoints)):
            minutes=int(timePoints[tp][:2])*60+int(timePoints[tp][3:])
            ind=insertL(timelist,minutes)
            if(ind==-1):
                return 0
            else:
                timelist.insert(ind,minutes)
        timelist.append(24*60+timelist[0])
        return min([timelist[i+1]-timelist[i] for i in range(len(timelist)-1)])
        
a=Solution()
print(a.findMinDifference(["00:00","10:59","14:24","12:10"]))