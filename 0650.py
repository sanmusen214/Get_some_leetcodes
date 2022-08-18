class Solution:
    # 质数必须得从一开始复制粘贴本身次数
    # 非质数质因数分解后，将某一质因数项整体看作另一项质数的1，由此，将分解质因数后的结果按照dp映射累加即可
    def minSteps(self, n: int) -> int:
        def is_prime(num):
            for i in range(2,num):
                if num%i==0:
                    # print(num, "is not prime")
                    return False
            # print(num," is prime")
            return True
        def to_split(num):
            # print("turn ",num,end=" ")
            result=[]
            while(num!=1):
                for i in range(2,int(num)+1):
                    if num%i==0:
                        result.append(i)
                        num/=i
                        break
            # print(" to: ",result)
            return result
        dp=[0,0,2]
        if(n==1):
            return 0
        if(n==2):
            return 2
        for ind in range(3,n+1):
            if(is_prime(ind)):
                dp.append(ind)
            else:
                pri_list=to_split(ind)
                total=0
                for each in pri_list:
                    total+=dp[each]
                dp.append(total)
        return dp[-1]
                
a=Solution()
print(a.minSteps(4))
print(a.minSteps(8))