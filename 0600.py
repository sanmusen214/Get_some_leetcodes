class Solution:
    # count=1
    def findIntegers(self, n: int) -> int:
    #     self.count=1
    #     def findint(nowstr):
    #         if(int(nowstr,2)>n):
    #             return
    #         # print(int(nowstr,2))
    #         self.count+=1
    #         findint(nowstr+"0")
    #         if(nowstr[-1]!="1"):
    #             findint(nowstr+"1")
    #     findint("1")
    #     return self.count
        
a=Solution()
for i in range(10):
    print(a.findIntegers(10**i))