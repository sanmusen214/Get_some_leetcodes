import heapq #最小堆
# 先用二分查找找到符合条件的成本，在其中找利润最大的那个
# 资金一直是增加的，上次符合的这次也一定符合，
# 所以按照成本排序，二分查找比现有资金大的第一个项目的下标，每次二分给定上次的结果作为左边界，提高查找效率。
# 把上次钱不够考虑，这次钱够了的项目往最大堆里添加来考虑赚了钱之后又可以新投资的项目
# 二分数组固定，last_end之前的那些添加到堆里面的肯定是能用的项目，项目从堆里pop后不影响二分数组last_end之的项目的二分查找
# 总而言之，二分数组只管哪些项目可用，将他们添加到堆，堆数组只管我现在要做哪个项目

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        def search(nums, target: int,left=-1) -> int:
            right=len(nums)
            while(left+1!=right):
                center=int((left+right)/2)
                if(nums[center][1]==target):
                    # 这里是二分找第一个大于所给元素的
                    left=center
                if(nums[center][1]>target):
                    right=center
                else:
                    left=center
            return right
        pro_inc=[[-profits[i],capital[i]] for i in range(len(profits))]
        pro_inc.sort(key=lambda each:each[1])
        print(pro_inc)
        last_end=0
        # 堆初始化为空
        minheap=[]
        heapq.heapify(minheap)
        # 每次资金增加后，把多出来可用的项目添加进堆
        for i in range(k):
            # 注意上次定位的last_end不能被染色，因此last_end-1，所以last_end初始化为0
            end=search(pro_inc,w,last_end-1)
            print("end=",end)
            # 没法赚钱直接gg
            if(end==0):
                break
            for ind in range(last_end,end):
                heapq.heappush(minheap,pro_inc[ind])
            if(not minheap):break
            maxearn=heapq.heappop(minheap)
            print("earn:",maxearn[0])
            w-=maxearn[0]
            last_end=end
        return w
    
a=Solution()
print(a.findMaximizedCapital(10,0,[1,2,3],[0,1,2]))
            