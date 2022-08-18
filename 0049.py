class Solution:
    def groupAnagrams(self, strs):
        abc=[0 for i in range(26)]
        table={}
        for i in range(len(strs)):
            abc_c=abc[::]
            for each_c in strs[i]:
                abc_c[ord(each_c)-97]+=1
            abc_c=tuple(abc_c)
            if abc_c not in table:
                table[abc_c]=[i]
            else:
                table[abc_c].append(i)
        # 处理异位词        
        return [[strs[j] for j in table[i]] for i in table]
a=Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))