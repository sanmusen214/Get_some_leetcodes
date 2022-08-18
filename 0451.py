class Solution:
    def frequencySort(self, s: str) -> str:
        countset={}
        for i in s:
            if i not in countset:
                countset[i]=1
            else:
                countset[i]+=1
        countlist=[[countset[a],a] for a in countset]
        countlist.sort(reverse=1)
        # print(countlist)
        strlist=[]
        for each in countlist:
            for i in range(each[0]):
                strlist.append(each[1])
        return ''.join(strlist)
a=Solution()
print(a.frequencySort("tree"))
