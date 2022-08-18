class Solution:
    def allPathsSourceTarget(self, graph):
        allpaths=[[0]]
        len_g=len(graph)
        resultpaths=[]0
        while(allpaths):
            thistime=allpaths[-1]
            allpaths.pop(-1)
            if(thistime[-1]==len_g-1):
                resultpaths.append(thistime)
                continue
            for nextnode in graph[thistime[-1]]:
                temp=thistime[::]
                temp.append(nextnode)
                allpaths.append(temp)
        return resultpaths
                
        
            
                
                
    
a=Solution()
