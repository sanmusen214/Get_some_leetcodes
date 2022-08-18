class Solution:
    def divide(self, dividend: int, divisor: int):
        if(dividend==-pow(2,31) and divisor==-1):  #溢出
            return pow(2,31)-1
        return in_piece_divide(dividend,divisor)
    
    
def in_piece_divide(top,below):
    if(top>=0):
        if(below>0):
            times=1
        else:
            times=-1
        if(below*times>top):  #如果除数乘最小商已经大于被除数，舍去小数
            return 0
        while(True):
            if(times*below<top):
                lasttimes=times  #存储上次底数
                times*=2
            elif(times*below==top):
                return times
            else:
                return lasttimes+in_piece_divide(top-lasttimes*below,below)
    if(top<0):
        if(below>0):
            times=-1
        else:
            times=1
        if(below*times<top):  #如果除数乘最小商已经大于被除数，舍去小数
            return 0
        while(True):
            if(times*below>top):
                lasttimes=times  #存储上次底数
                times*=2
            elif(times*below==top):
                return times
            else:
                return lasttimes+in_piece_divide(top-lasttimes*below,below)
    
    
    

                


                
            
a=Solution()
print(a.divide(-7,-3))
