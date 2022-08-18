class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # 记录每个点入度和出度 点：【入点们，出点们】
        count=dict()
        # 筛选无入度的点作为起始点，BFS拓扑排序
        noinnodes=set([i for i in range(numCourses)])
        for each in prerequisites:
            fromnode=each[1]
            tonode=each[0]
            if(tonode in noinnodes):
                noinnodes.remove(tonode)
            count[fromnode]=[count.get(fromnode,[[],[]])[0],count.get(fromnode,[[],[]])[1]+[tonode]]
            count[tonode]=[count.get(tonode,[[],[]])[0]+[fromnode],count.get(tonode,[[],[]])[1]]
        
        # 把与别的课程没关系的加进去
        for course in range(numCourses):
            if(course not in count):
                count[course]=[[],[]]
                noinnodes.add(course)
                
        # print(count)
        allvisited=[]
        while(noinnodes):
            # 选起始点
            nodenow=noinnodes.pop()
            allvisited.append(nodenow)
            # 移除该点，减少它指向的点的入度
            for tons in count[nodenow][1]:
                count[tons][0].remove(nodenow)
                # 如果这些点入度为0，添加到队列中
                if(len(count[tons][0])==0):
                    noinnodes.add(tons)
        if(len(allvisited)!=numCourses):
            return []
        return allvisited
        
a=Solution()
print(a.findOrder(5,[]))
