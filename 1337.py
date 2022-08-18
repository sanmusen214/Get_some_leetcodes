class Solution:
    def kWeakestRows(self, mat, k: int):
        ref={}
        for r in range(len(mat)):
            num=0
            for i in mat[r]:
                if i==1:
                    num+=1
                else:
                    break
            if num in ref:
                ref[num].append(r)
            else:
                ref[num]=[r]
        result=[]
        times=k
        for low in sorted(ref.keys()):
            for n in ref[low]:
                if k==0:
                    break
                result.append(n)
                k-=1
        return result
a=Solution()
print(a.kWeakestRows([[1,1,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1]],3))
        