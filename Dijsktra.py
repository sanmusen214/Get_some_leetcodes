import bisect
def dijstra(self,board,source,target=None):
    '''
    邻接矩阵放距离,-1无连接，对角默认-1，源点
    '''
    concern_his=[source] # 确定下来的顺序
    white={source:[0,source]} # 已确定的点， {自己：[距离源点总距离，上家]}
    gray=[] # 未确定但可到达的点 [[距离源点总距离，自己，上家],[距离源点总距离，自己，上家]] # 找最短距离，找某个点
    # 初始化gray
    for i in range(len(board[source])):
        if(board[source][i]!=-1):
            bisect.insort(gray,[board[source][i],i,source])
    while(gray):
        # 弹出最短距离的gray点
        dis,me,father=gray.pop(0)
        if(me in white): #*每次新弹出之后判断被弹出点是否已确定（在white里即可，不区分新加点在不在grayset里，不用查找更新gray里某个点的距离数据
            continue
        # 确定这个点放到white里
        white[me]=[dis,father]
        concern_his.append(me)
        # 如果这个就是目标点，直接结束
        if(target==me):
            break
        # 更新与这个点相邻的点的距离,此处除了使用二维列表，也可以使用一个自定义的点对象来只用一维列表
        for nextnodeind in range(len(board[me])):
            # 与ind点没有连结边，略过
            if(board[me][nextnodeind]==-1):
                continue
            # ind（相邻点已经确定（在white中，略过
            if(nextnodeind in white):
                continue
            # 从源点到刚确定下来的nextnodeind的距离=从原点到这个点的距离+这个点到nextnodeind的距离
            newdis=white[me][0]+board[me][nextnodeind]
            # 将这个点的信息排序插入gray列表
            bisect.insort(gray,[newdis,nextnodeind,me])
    return {'history':concern_his,'result':white}