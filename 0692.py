class Solution:
    def topKFrequent(self, words, k: int):
        #数单词出现次数
        #对出现次数和单词排序
        #可用元组多key排序
        f=[(words.count(each),each) for each in list(set(words))]
        f.sort(key=lambda s:(-s[0],s[1]))
        return [f[each][1] for each in range(k)]
                
            
         
                    
a=Solution()
print(a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
2))
print(a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))
