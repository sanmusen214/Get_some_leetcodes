class Solution:
    def shortestDistanceColor(self, colors: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        t1,t2,t3=[float("-inf"),float("-inf"),float("-inf")]
        nearest=[[float("inf"),float("inf"),float("inf")] for i in range(len(colors))]
        for i in range(len(colors)):
            if(colors[i]==1):
                t1=i
            elif(colors[i]==2):
                t2=i
            elif(colors[i]==3):
                t3=i
            nearest[i]=[min(nearest[i][0],i-t1),min(nearest[i][1],i-t2),min(nearest[i][0],i-t3)]
        t1,t2,t3=float("inf"),float("inf"),float("inf")
        for i in range(len(colors)-1,-1,-1):
            if(colors[i]==1):
                t1=i
            elif(colors[i]==2):
                t2=i
            elif(colors[i]==3):
                t3=i
            nearest[i]=[min(t1-i,nearest[i][0]),min(t2-i,nearest[i][1]),min(t3-i,nearest[i][2])]
        return [nearest[each[0]][each[1]-1] if nearest[each[0]][each[1]-1]!=float("inf") else -1 for each in queries]

a=Solution()
print(a.shortestDistanceColor([1,1,2,1,3,2,2,3,3],[[1,3],[2,2],[6,1]]))
print(a.shortestDistanceColor([1,2],[[0,3]]))

        