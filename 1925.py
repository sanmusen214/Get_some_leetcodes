class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        relation_set={}
        for each in relation:
            if(relation_set.get(each[0])):
                relation_set[each[0]].append(each[1])
            else:
                relation_set[each[0]]=[each[1]]
        # print("relation",relation_set)
        if(not relation_set.get(0)):return 0
        nowset={a:1 for a in relation_set[0]}
        # print(nowset)
        times=0
        while(times<k-1):
            newset={}
            for each in nowset:
                if(relation_set.get(each)):
                    for e in relation_set[each]:
                        if(newset.get(e)):
                            newset[e]+=nowset[each]
                        else:
                            newset[e]=nowset[each]
            # print(newset)
            nowset=newset
            times+=1
        return nowset[n-1] if nowset.get(n-1) else 0
                
                
                    
a=Solution()
print(a.numWays(3,[[0,2],[0,1],[1,2],[2,1],[2,0],[1,0]],1))#1
print(a.numWays(5,[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]],3))#3


