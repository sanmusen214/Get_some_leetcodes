#用列表模拟单调栈
#栈底到栈顶递增
class MonotoneStack:
    def __init__(self,numlist=[]):
        self.stack=[]
        self.index=-1
        self.momap=dict()
        for i in numlist:
            self.push(i)
    def push(self,num):
        self.index+=1
        # 为空直接入栈
        if(len(self.stack)==0):
            self.stack.append([num,self.index])
            self.momap[self.index]=-1
        # 栈顶小于等于当前数，直接入栈
        elif(self.stack[-1][0]<=num):
            self.stack.append([num,self.index])
            self.momap[self.index]=-1
        # 栈顶大于当前数，循环pop直到小于等于当前数
        else:
            while(self.stack and self.stack[-1][0]>num):
                cur=self.stack.pop()
                # 对于下标x向右，最靠近它的小于它的数的下标是y
                self.momap[cur[1]]=self.index
            self.stack.append([num,self.index])
    def getMap(self):
        '''
            得到坐标映射：
            下标key在数组中，右边最近的且小于它的数字的下标是value，如果没有则value为-1
        '''
        return self.momap
    
a=MonotoneStack([2,1,5,6,2,3])
print(a.getMap())
            
                