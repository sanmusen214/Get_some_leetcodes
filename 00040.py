class Solution:
    #与0039类似，不同的是约束每个数字的最多使用次数。通过把0039的代码转换过来一下就可以解决
    #将输入计数，然后set化，约束每个数字最多使用次数为相应的count
    def combinationSum2(self, candidates, target):
        def trythis(num_after_this,nowtotal,now_list):
            now_list=now_list.copy()
            if(nowtotal==target):
                results.append(now_list)
            if(nowtotal>=target or num_after_this>=len(candidates)):
                return
            use_time=0
            while(nowtotal<=target and use_time<=num_count[candidates[num_after_this]]):
                trythis(num_after_this+1,nowtotal,now_list)
                use_time+=1
                nowtotal+=candidates[num_after_this]
                now_list.append(candidates[num_after_this])
        results=[]
        num_set=set(candidates)
        num_count={i:candidates.count(i) for i in num_set}
        candidates=list(num_set)
        print(num_count)
        trythis(0,0,[])
        return results





a=Solution()
print(a.combinationSum2([10,1,2,7,6,1,5],8))
