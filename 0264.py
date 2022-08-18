class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        want_to_mul2_least = 0
        want_to_mul3_least = 0
        want_to_mul5_least = 0
        for i in range(n-1):
            res.append(min(res[want_to_mul2_least]*2,res[want_to_mul3_least]*3,res[want_to_mul5_least]*5))
            if res[-1] == res[want_to_mul2_least]*2:
                want_to_mul2_least += 1
            if res[-1] == res[want_to_mul3_least]*3:
                want_to_mul3_least += 1
            if res[-1] == res[want_to_mul5_least]*5:
                want_to_mul5_least += 1
        return res[-1]
    
m=Solution()
print(m.nthUglyNumber(10))
