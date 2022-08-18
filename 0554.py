class Solution:
    def leastBricks(self, wall) -> int:
        if(sum(wall[0])==1):return len(wall)
        blank={}
        for i in range(len(wall)):
            ptr=-1
            for w in wall[i][:-1]:
                ptr+=w
                if(ptr in blank.keys()):
                    blank[ptr]+=1
                else:
                    blank[ptr]=1
        mx=0
        for v in blank.values():
            if v>mx: mx=v
        return len(wall)-mx
        
        
            
                    
            
                    
    

                

a=Solution()
print(a.leastBricks([[1],[1],[1]]))
print(a.leastBricks([[6],[6],[2,4],[6],[1,2,2,1],[6],[2,1,2,1],[1,5],[4,1,1],[1,4,1],[4,2],[3,3],[2,2,2],[5,1],[5,1],[6],[4,2],[1,5],[2,3,1],[4,2],[1,1,4],[1,3,1,1],[2,3,1],[3,3],[3,1,1,1],[3,2,1],[6],[3,2,1],[1,5],[1,4,1]]))
#17
print(a.leastBricks([[100000000],[100000000],[100000000]]))
