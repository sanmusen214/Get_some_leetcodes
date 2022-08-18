class RecentCounter:

    def __init__(self):
        # 存储当前所有t
        self.ts=[]
        # 上次找的下标
        self.lasti=0

    def ping(self, t: int) -> int:
        # print("self.ts: ",self.ts)
        # print("last i: ",self.lasti)
        self.ts.append(t)
        i=self.lasti
        while(i<=t):
            if(self.ts[i]>=t-3000):
                self.lasti=i
                break
            i+=1
        return len(self.ts)-self.lasti
                
    

a=RecentCounter()
print(a.ping(1178))
print(a.ping(1483))
print(a.ping(1563))
print(a.ping(4054))
print(a.ping(4152))

