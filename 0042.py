class Solution:
    def wtheight(self):
        self.wtheight
    def trap(self, height) -> int:
        # height.insert(0,-1)
        # height.insert(len(height),-1)
        #dp
        def addline(hlist_ptr,line,v):
            '''
            试图将line添加到hlist右边，看v会变成多少，
            两种情况，一种v会增加，一种v不变。
            hlist在v增加之后应该被填充
            '''
            if(line<=height[hlist_ptr-1]):
                return v
            fir_hest_ptr=hlist_ptr-1
            for i in range(hlist_ptr-2,-1,-1):
                if(height[i]>=line):
                    fir_hest_ptr=i
                    break
                if(height[i]>=height[fir_hest_ptr]):
                    fir_hest_ptr=i
            if(fir_hest_ptr==-1):return v
            waterline=line if line<=height[fir_hest_ptr] else height[fir_hest_ptr]
            for i in range(fir_hest_ptr+1,hlist_ptr):
                v+=waterline-height[i]
                height[i]=waterline
            return v
        
        if(len(height)==0):return 0
        dp=[0 for i in range(len(height))]
        for i in range(1,len(height)):
            dp[i]=addline(i,height[i],dp[i-1])
        return dp[len(height)-1]
                    
            
                    
            
                    
    

                

a=Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))#6
print(a.trap([4,2,0,3,2,5]))#9
print(a.trap([4,2,3]))#1
print(a.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))#83
print(a.trap([]))
#174801674
