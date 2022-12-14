class Solution:
    # 2^16=(2^2)^8=((2^2)^2)^4=(((2^2)^2)^2)^2=((((2^2)^2)^2)^2)^1 i为1/2后为0结束递归
    # 2^21=(2^2)^10*2^1=((2^2)^2)^5*2^1=(2^2^2)^2^2*2^1*(2^2^2)=(2^2^2)^2^2^1*2^1*(2^2^2)  出现多少次奇数幂就乘上多少个当时的底
    # 解决了负数幂爆栈，当
    def myPow(self, x: float, n: int) -> float:
        res=1
        i=n
        while(i!=0):
            if(i%2!=0):
                res*=x
            x*=x
            i=int(i/2)
        return 1/res if n<0 else res 