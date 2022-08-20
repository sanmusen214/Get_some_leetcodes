class Solution:
    def nextGreaterElements(self, nums: 'List[int]'):
        stack=[]
        res=[-1 for i in range(len(nums))]
        def push(num,ind):
            # 把小于当前的pop出去，并更新被pop出去的之后的最大值
            while(stack and num>stack[-1][0]):
                oldnum,oldind=stack.pop()
                if(oldind>=0 and oldind<len(nums)):
                    res[oldind]=num
            stack.append([num,ind])
        # 传入两次模拟循环
        for i in range(len(nums)):
            push(nums[i],i)
        for i in range(len(nums)):
            push(nums[i],i+len(nums))
        return res