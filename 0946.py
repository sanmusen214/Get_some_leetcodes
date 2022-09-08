class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:
        stack=[]
        pt1=pt2=0
        while(1):
            if(pt1==len(pushed)):
                break
            stack.append(pushed[pt1])
            pt1+=1
            # 尝试pop
            while(pt2<len(popped) and stack and popped[pt2]==stack[-1]):
                stack.pop()
                pt2+=1
        if(not stack):
            return True
        return False

a=Solution()
print(a.validateStackSequences([1,2,3,4,5], popped = [4,5,3,2,1]))# T
print(a.validateStackSequences([1,2,3,4,5], popped = [4,3,5,1,2])) # F