class Solution:
    def longestValidParentheses(self, s: str) -> int:
        listp=dramatic(list(s))
        longest=0
        count=0
        for i in listp:
            if(i=="0"):
                count+=1
            else:
                if(count>longest):
                    longest=count
                count=0
            if(count>longest):  #最后一遍无else仍需判断count
                longest=count
        return longest

def dramatic(listr):
    done=0
    for i in range(len(listr)):
        if(listr[i]=="("):
            for j in range(i+1,len(listr)):
                if(listr[j]=="0"):
                    continue
                if(listr[j]=="("):
                    break
                if(listr[j]==")"):
                    listr[i]=listr[j]="0"
                    done=1
                    break
    if(done==1):
        return dramatic(listr)
    if(done==0):
        return listr 
                
                         
# print(dramatic(["(",")","(","(",")",")","(","("]))
a=Solution()
print(a.longestValidParentheses("(()"))

