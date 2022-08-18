class Solution:
    # ans = [1,2,3,8,10,36,41,132]
    count=0
    def countArrangement(self, n: int) -> int:
        self.count=0
        def trythis(num,numlist,lastlist):
            if(num%(len(numlist)+1)!=0 and (len(numlist)+1)%num!=0):#不符合
                return 
            if(len(lastlist)==0):#符合
                self.count+=1
                print(numlist+[num])
                return
            for i in range(len(lastlist)):#继续dfs
                trythis(lastlist[i],numlist+[num],lastlist[:i]+lastlist[i+1:])
        for eachi in range(1,n+1):
            startlist=[i for i in range(1,n+1)]
            startlist.pop(eachi-1)
            print("start try{}".format(eachi),end="")
            print(" ",startlist)
            trythis(eachi,[],startlist)
        return self.count
    
    
a=Solution()
print(a.countArrangement(4))
        

            