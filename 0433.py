class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        def dis(b1,b2):
            count=0
            for i in range(8):
                if(b1[i]!=b2[i]):
                    count+=1
            return count
        transtable={}
        for i in range(len(bank)):
            for j in range(len(bank)):
                diff=dis(bank[i],bank[j])
                if(diff==1):
                    resbefore=transtable.get(bank[i],[])
                    resbefore.append(bank[j])
                    transtable[bank[i]]=resbefore
        # 开头到bank
        resbefore=transtable.get(start,[])
        for each in bank:
            if(dis(each,start)==1):
                if(each not in resbefore):
                    resbefore.append(each)
        transtable[start]=resbefore
        # print(transtable)
        def bfs(genelist,times):
            newlist=[]
            for gene in genelist:
                if(gene in transtable):
                    # print("old: ",transtable[gene])
                    for each in transtable[gene]:
                        if(each==end):
                            return times
                        if(each not in newlist):
                            newlist.append(each)
            # print(times,newlist)
            if(len(newlist)==0 or times>8):
                return -1
            return bfs(newlist,times+1)
        return bfs([start],1)
    
a=Solution()
# print(a.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(a.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(a.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))
print(a.minMutation("AAAAAAAA","CCCCCCCC",["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]))
