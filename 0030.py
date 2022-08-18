class Solution:
    def findSubstring(self, s: str, words):
        sptr=0
        relist=[]
        lenw=0
        for i in words:
            lenw+=len(i)
        while(True):
            if(sptr+lenw>len(s)):
                break
            start,end=fitwordfst(s[sptr:],words)
            if(sptr+start==len(s)):
                break
            sptr+=start
            if(whether_fitwordsall(s[sptr:],words.copy())):
                relist.append(sptr)
            sptr+=1
        return relist


def whether_fitwordsall(s,wordlist):
    while(True):
        f=0
        if(len(wordlist)==0):
            return True
        for i in wordlist:
            if(s.find(i)==0):
                wordlist.remove(i)
                s=s[len(i):]
                f=1
                break
        if(f==0):
            return False
        

def fitwordfst(s,words): #在s中用words找，返回最左的单词开头末尾地址
    fstptr=len(s)
    which=''
    for i in words:
        if(s.find(i)>=0 and s.find(i)<fstptr):
            fstptr=s.find(i)
            which=i
    return fstptr,fstptr+len(which)
            
    
                
            
a=Solution()
print(a.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))#6,9,12
print(a.findSubstring("aaaaaaaaaaaaaa",["aa","aa"]))#0-10
print(a.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
print(a.findSubstring("a",["a"]))#0
