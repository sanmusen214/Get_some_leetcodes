class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        # 按照直觉来说不应该将最大与最小放一条船上。
        # 但是并无大碍。这道题限制一条船最多坐两人和限制总重。
        # 假如a,b,c,d四个人体重递增，b+d<=limit 这时可能会将bd放一起，把最轻的a留给比较轻的c留有余裕。
        # 以上是担心bc二人一个船坐不下
        # 但是，c体重小于d，既然bd可坐一条船上，那么bc肯定也能坐一条船上。所以担心无效
        # 
        # 如果限制一条船的重量而不限制人数，则应该考虑余裕（每条船应该尽可能坐满）
        # limit=15,[2,2,3,5,8,10]
        # 如果依旧最大和最小们坐则是[2,2,10][3,8][5]
        # 考虑余裕[2,3,10][2,5,8]
        people.sort()
        left=0
        right=len(people)-1
        count=0
        while(left<right):
            if(people[right]+people[left]<=limit):
                left+=1
            right-=1
            count+=1
        if(left==right):
            count+=1
        return count
        
            
                
                
    
a=Solution()
print(a.numRescueBoats([3,2,2,1],3))