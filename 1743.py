class Solution:
    def restoreArray(self, adjacentPairs):
        # nowlist=[adjacentPairs[0][0],adjacentPairs[0][1]]
        # headtail=[adjacentPairs[0][0],adjacentPairs[0][1]]
        # adjacentPairs.pop(0)
        # while(len(adjacentPairs)>0):
        #     for i in range(len(adjacentPairs)-1,-1,-1):
        #         pair=adjacentPairs[i]
        #         if(pair[0] in headtail or pair[1] in headtail):
        #             if(pair[0] in headtail):
        #                 if(pair[0]==headtail[0]):
        #                     nowlist.insert(0,pair[1])
        #                     headtail[0]=pair[1]
        #                 else:
        #                     nowlist.append(pair[1])
        #                     headtail[1]=pair[1]
        #             else:
        #                 if(pair[1]==headtail[0]):
        #                     nowlist.insert(0,pair[0])
        #                     headtail[0]=pair[0]
        #                 else:
        #                     nowlist.append(pair[0])
        #                     headtail[1]=pair[0]
        #             adjacentPairs.pop(i)
        # return nowlist
        
        numset={}
        for each in adjacentPairs:
            for i in range(2):
                if(each[i] in numset):
                    numset[each[i]].append(each[1-i])
                else:
                    numset[each[i]]=[each[1-i]]
        numlist=[]
        for k in numset:
            nowp=numset[k]
            if(len(nowp)==1):
                numlist+=[k,nowp[0]]
                break
        while(1):
            if(len(numset[numlist[-1]])==1):break
            numset[numlist[-1]].remove(numlist[-2])
            numlist.append(numset[numlist[-1]][0])
        return numlist
    

def addtwo(a,b):

    return a+b
            
a=Solution()
print(a.restoreArray([[1,2],[3,4],[3,2]]))
