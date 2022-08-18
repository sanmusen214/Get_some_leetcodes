class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        sumlist=[0]
        sumnow=0
        for i in arr:
            sumnow+=i
            sumlist.append(sumnow)
        total=0
        for i in range(len(sumlist)):
            len_n=1
            while(len_n<=i):
                print("add %d"%(sumlist[i]-sumlist[i-len_n]))
                total+=(sumlist[i]-sumlist[i-len_n])
                len_n+=2
        return total

a=Solution()
print(a.sumOddLengthSubarrays([1,4,2,5,3]))