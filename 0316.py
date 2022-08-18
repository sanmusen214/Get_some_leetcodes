class Solution:
    def removeDuplicateLetters(self, s: str):
        # 记录出现次数
        count=dict()
        for each in s:
            count[each]=count.get(each,0)+1
        # 单调栈
        stack=[]
        # 在栈里的
        stackset=set()
        for w in s:
            # 如果已经在里面了，就不放进去
            if(w not in stackset):
                # 如果当前大于栈顶或栈为空直接放
                if(len(stack)==0 or w>stack[-1]):
                    stack.append(w)
                    stackset.add(w)
                else:
                    # 如果当前小于等于栈顶，考虑pop出栈顶
                    while(len(stack)!=0 and w<=stack[-1] and count[stack[-1]]>0):
                        sp=stack.pop()
                        stackset.remove(sp)
                    stack.append(w)
                    stackset.add(w)
            count[w]-=1
        return ''.join(stack)

a=Solution()
print(a.removeDuplicateLetters("cbacdcbc"))
print(a.removeDuplicateLetters("bbcaac"))