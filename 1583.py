class Solution:
    def unhappyFriends(self, n: int, preferences: "List[List[int]]", pairs: "List[List[int]]") -> int:
        if n==2:return 0
        count=0
        had={}
        for i in range(len(pairs)):
            for j in range(i+1,len(pairs)):
                x,y=pairs[i][0],pairs[i][1]
                u,v=pairs[j][0],pairs[j][1]
                for tis in range(2):
                    x,y=y,x
                    for tiess in range(2):
                        u,v=v,u
                        print("this time:{},{}  {},{}".format(x,y,u,v))
                        if(preferences[x].index(u)<preferences[x].index(y) and preferences[u].index(x)<preferences[u].index(v)):
                            print("{} {},{} {}".format(x,y,u,v))
                            had[x]=1
                            count+=1
                        if(preferences[u].index(x)<preferences[u].index(v) and preferences[x].index(u)<preferences[x].index(y)):
                            print("{} {},{} {}".format(u,v,x,y))
                            had[u]=1
                            count+=1
        return len(had.keys())

a=Solution()
print(a.unhappyFriends(4,[[1,3,2],[2,3,0],[1,3,0],[0,2,1]],[[1,3],[0,2]]))