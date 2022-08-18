class Solution:
    def groupAnagrams(self, strs):
        alltypes=[]
        finalout=[]
        for each in range(len(strs)):
            countnums=[0 for i in range(26)]
            for c in strs[each]:
                countnums[ord(c)-97]+=1
            if(countnums not in alltypes):
                alltypes.append(countnums)
                finalout.append([strs[each]])
            else:
                finalout[alltypes.index(countnums)].append(strs[each])
        return finalout
                
        
        
                
                
a=Solution()
print(a.groupAnagrams(["asa","saa","rew","saa"]))
