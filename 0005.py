class Solution:
    def longestPalindrome(self, s: str) -> str:
        tru=1
        left=0
        right=0
        mostleft=0
        mostright=0
        for c in [float(i)/2 for i in range(2*len(s))]:
            left=c
            right=c
            while(tru==1):
                left=left-0.5 if left%1==0.5 else left-1
                right=right+0.5 if right%1==0.5 else right+1
                left=int(left)
                right=int(right)
                if(left<0 or right>=len(s) or not s[left] is s[right]):
                    left=left+1
                    right=right-1
                    break
            if(right+1-left>mostright+1-mostleft):
                mostright=right
                mostleft=left
        return s[mostleft:mostright+1]
                
                
                    
a=Solution()
print(a.longestPalindrome("cbbd"))

