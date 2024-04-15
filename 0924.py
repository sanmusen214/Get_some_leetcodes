from typing import List


class Solution:

    def grandFather(self, nodes, node):
        # 找到节点的祖父节点
        print("The father of ",node)
        while(nodes[node][0]>=0):
            # print(nodes, node)
            node = nodes[node][0]
        print("        is",node)
        return node

    def addTo(self, nodes, fromnode, tonode):
        fathernode1 = self.grandFather(nodes, fromnode)
        fathernode2 = self.grandFather(nodes, tonode)
        if fathernode1 == fathernode2:
            return
        nodes[fathernode2][0] += nodes[fathernode1][0]
        # 合并感染节点
        if nodes[fathernode1][1] == -2 or nodes[fathernode2][1] == -2 or (nodes[fathernode1][1] >= 0 and nodes[fathernode2][1] >= 0):
            newBadCounts = -2
        else:
            # 只有一个有值
            newBadCounts = nodes[fathernode1][1] if nodes[fathernode1][1] >= 0 else nodes[fathernode2][1]
        nodes[fathernode2][1] = newBadCounts
        nodes[fathernode1][0] = fathernode2
        print("after combine ", fromnode, "to", tonode, ". Result is ",nodes)
        
    
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # 创建连通图
        nodes = [[-1, -1] for i in range(len(graph))]
        # 初始化initial
        for badnode in initial:
            print("badnode", badnode)
            nodes[badnode][1] = badnode
            print(nodes)
        print("Initial nodes", nodes)
        for row in range(len(graph)):
            print("find row", row)
            tofather = self.grandFather(nodes, row)
            for col in range(row+1, len(graph)):
                if graph[row][col] == 1:
                    self.addTo(nodes, col, tofather)
        print(nodes)
        # 找到最大的那个
        tempmaxcount = -1
        tempminind = float("inf")
        for each in nodes:
            if each[0] < 0 and abs(each[0])>=tempmaxcount:
                if each[1] >= 0 and (each[1] < tempminind or abs(each[0])>tempmaxcount):
                    tempminind = each[1]
                    tempmaxcount = abs(each[0])
        return tempminind if tempminind != float("inf") else min(initial)
        
if __name__ == "__main__":
    s = Solution()
    print(s.minMalwareSpread([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,1,1]],[3,1]))