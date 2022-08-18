class Solution:
    def isRectangleCover(self, rectangles: "List[List[int]]") -> bool:
        areas=0
        pair_set=set()
        for rec in rectangles:
            # print(pair_set)
            areas+=((rec[2]-rec[0])*(rec[3]-rec[1]))
            for i in [rec[0],rec[2]]:
                for j in [rec[1],rec[3]]:
                    # print((i,j))
                    if (i,j) in pair_set:
                        pair_set.remove((i,j))
                    else:
                        pair_set.add((i,j))
        # print(pair_set)
        listx=set()
        listy=set()
        if(len(pair_set)==4):
            for eachp in pair_set:
                listx.add(eachp[0])
                listy.add(eachp[1])
            if(len(listx)==2 and len(listy)==2):
                if (max(listx)-min(listx))*(max(listy)-min(listy))==areas:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
a=Solution()
print(a.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))