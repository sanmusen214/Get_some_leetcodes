class Solution:
    # 递归，先处理剪枝，然后处理保存答案，然后处理下一层递归
    def combinationSum(self, candidates, target):
        def trythis(num_after_this,nowtotal,now_list):
            now_list=now_list.copy()
            if(nowtotal==target):
                results.append(now_list)
            if(nowtotal>=target or num_after_this>=len(candidates)):
                return
            while(nowtotal<=target):
                trythis(num_after_this+1,nowtotal,now_list)
                nowtotal+=candidates[num_after_this]
                now_list.append(candidates[num_after_this])
        results=[]
        trythis(0,0,[])
        return results





a=Solution()
print(a.combinationSum([2,3,5],8))
