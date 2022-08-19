class Solution:
    def busyStudent(self, startTime: 'List[int]', endTime: 'List[int]', queryTime: int) -> int:
        # +1防止越下标
        preList=[0 for i in range(1001)]
        for i in range(len(startTime)):
            # 全体前向挪1，start,end范围从[1,1000]=>[0,999]
            start=startTime[i]-1
            end=endTime[i]-1
            preList[start]+=1
            # 双闭区间，end当天过去后计算-1,end下标范围[1,1000]
            preList[end+1]-=1
        preSum=0
        for i in range(queryTime):
            preSum+=preList[i]
        return preSum
