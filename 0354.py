import bisect


class Solution:
    # https://labuladong.gitee.io/algo/3/25/70/
    def maxEnvelopes(self, envelopes: 'List[List[int]]') -> int:
        envelopes.sort(key=lambda x:x[0]*100001-x[1])
        envelopes = [each[1] for each in envelopes]
        piles=[]
        for i in range(len(envelopes)):
            if(not piles or envelopes[i]>piles[-1]):
                piles.append(envelopes[i])
            else:
                ind=bisect.bisect_left(piles,envelopes[i])
                piles[ind]=envelopes[i]
            print(piles)
        return len(piles)

a=Solution()
print(a.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))#3