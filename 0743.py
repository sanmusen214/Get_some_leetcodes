class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        ref={}
        for each in times:
            if each[0] not in ref:
                ref[each[0]]={each[1]:each[2]}
            else:
                ref[each[0]][each[1]]=each[2]
        hadtravel={k:0}
        nowtravel=[k]
        while(nowtravel):
            nexttravel=[]
            for node in nowtravel:
                if node in ref:
                    for nextnode in ref[node]:
                        if nextnode not in hadtravel or hadtravel[node]+ref[node][nextnode]<hadtravel[nextnode]:
                            hadtravel[nextnode]=hadtravel[node]+ref[node][nextnode]
                            nexttravel.append(nextnode)
                            # print(nexttravel)
            nowtravel=nexttravel
        if(len(list(hadtravel.keys()))==n):
            return max(hadtravel.values())
        return -1
                        
            
            
            
a=Solution()
print(a.networkDelayTime([[1,2,1],[2,3,1],[3,1,1]],3,1))
        