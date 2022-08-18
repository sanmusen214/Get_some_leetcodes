class Solution:
    def findWords(self, words):
        lines={}
        for i in "qwertyuiop":
            lines[i]=0
        for j in "asdfghjkl":
            lines[j]=1
        for k in "zxcvbnm":
            lines[k]=2
        res=[]
        for w in words:
            ww=w.lower()
            # print(ww)
            def check(word):
                nowl=-1
                for c in word:
                    if(nowl==-1):
                        nowl=lines[c]
                    elif(nowl!=lines[c]):
                        return False
                return True
            if(check(ww)):
                res.append(w)
            
        return res
a=Solution()
print(a.findWords(["Hello","Alaska","Dad","Peace"]))