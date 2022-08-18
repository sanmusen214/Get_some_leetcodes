class Solution:
    # 根据queries算arr连续异或结果，利用异或的相消特性，
    # 可以先求出reflist列表，代表arr连续异或直到末尾
    # 计算queries只需将relist提出两相消并加上开头即可
    def xorQueries(self, arr, queries):
        arr=[0]+arr
        reflist=[0]
        for i in range(len(arr)-1):
            reflist.append(reflist[i]^arr[i+1])
        reflist.pop(0)
        relist=[reflist[each[0]]^reflist[each[1]]^arr[each[0]+1] for each in queries]
        return relist

a=Solution()
print(a.xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))
