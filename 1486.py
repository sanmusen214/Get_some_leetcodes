class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        total=0
        for i in [start+2*i for i in range(n)]:
            total^=i
        return total

                

a=Solution()
print(a.xorOperation(10,5))
