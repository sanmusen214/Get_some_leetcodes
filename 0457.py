class Solution:
    def circularArrayLoop(self, nums: "List[int]") -> bool:
        state=[-1 for i in range(len(nums))]
        meetcount=0
        def move(stand,step):
            target=(stand+step)%(len(nums))
            # print("from {} walks {} is {}".format(stand,step,target))
            return target
        for i in range(len(nums)):
            small=False
            if(state[i]!=-1):#小圈大要确认一遍，防止差集处有方向变更
                small=True
            foot=i
            state[foot]=i#状态数组标记
            face=True if nums[foot]>0 else False#False左True右 记录当前移动方向
            facechanged=False#记录方向是否转过
            while(1):
                # print(state)
                newfoot=move(foot,nums[foot])
                if(newfoot==foot):#循环长度为1特例
                    break
                if(state[newfoot]==i):#newfoot已经在这次路途走过
                    if(facechanged):
                        break
                    else:
                        return True
                elif(state[newfoot]==-1 or small):#newfoot从没有被走过 或 在其他路途走过 大圈小无需再走 必须要小圈大才继续
                    state[newfoot]=i#标记
                    if(face and nums[newfoot]<0 ) or (not face and nums[newfoot]>0):
                        facechanged=True
                elif(state[newfoot]!=-1 and not small):
                    break
                foot=newfoot
        return False
                
a=Solution()
print(a.circularArrayLoop([2,-1,1,2,2]))#t
print(a.circularArrayLoop([-1,2]))#f
print(a.circularArrayLoop([-2,1,-1,-2,-2]))#f
print(a.circularArrayLoop([-1,-2,-3,-4,-5]))#f
            
