class Solution:
    def nthSuperUglyNumber(self, n: int, primes: "List[int]") -> int:
        #不可能有未来生产出来的成为比当前堆里最小的还小，因为当前拿出来的是堆里最小的，乘正数之后只会变大。堆的特性使得每次拿出来的都是最紧邻的最小值。
        import heapq
        #最小堆，初始化为1
        heap = [1]
        heapq.heapify(heap)
        for j in range(n - 1):  
            print("times: ",j)
            #pop出堆顶最小元素
            curr = heapq.heappop(heap)
            print("first pop: ",curr)
            #heap[0]查看堆中最小值
            while heap and curr == heap[0]:
                # while 此处是去除重复的最小丑数
                curr = heapq.heappop(heap)
                print("while pop: ",curr)
            #重新将curr*各个prime入堆
            print("final pop: ",curr)
            for prime in primes:
                heapq.heappush(heap, (curr * prime))
        return heapq.heappop(heap)
a=Solution()
print(a.nthSuperUglyNumber(10,[2,3,7]))