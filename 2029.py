class Solution:
    def stoneGameIX(self, stones) -> bool:
        #0->1,2
        #1->0,1
        #2->0,2
        mlist={0:0,1:0,2:0}
        for i in range(len(stones)):
            stones[i]==stones[i]%3
            mlist[stones[i]]+=1
        if(mlist.get(0)%2==0):
            return mlist.get(1)!=0 and mlist.get(2)!=0
        return abs(mlist.get(2)-mlist.get(1))>2
        