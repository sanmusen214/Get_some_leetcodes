class Solution:
    table={}
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.table={}
        def outof(x,y):
            if(x<0 or x>n-1 or y<0 or y>n-1):
                return True
            return False
        def deepin(x,y,step):
            if(step==0):
                if(not outof(x,y)):
                    return 1
                else:
                    return 0
            if(outof(x,y)):
                return 0
            if((x,y,step) in self.table):
                return self.table[(x,y,step)]
            inboard=0
            for i in range(-2,3):
                if(i==0):continue
                if(abs(i)==2):
                    for j in range(-1,2,2):
                        inboard+=deepin(x+i,y+j,step-1)
                if(abs(i)==1):
                    for j in range(-2,3,4):
                        inboard+=deepin(x+i,y+j,step-1)
            self.table[(x,y,step)]=inboard
            return inboard
        if(k!=0):
            return deepin(row,column,k)/(8**k) 
        else:
            return deepin(row,column,k)/1

            
a=Solution()
print(a.knightProbability(3,1,0,0)) #0.25
print(a.knightProbability(3,2,0,0)) #0.0625
print(a.knightProbability(3,3,0,0)) #0.01562
print(a.knightProbability(3,1,1,1)) #0.0


