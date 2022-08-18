# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version==2:return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(isBadVersion(1)):return 1
        l=1
        r=n
        while(1):
            c=int((l+r+1)/2)
            if(not isBadVersion(c-1) and isBadVersion(c)):
                return c
            if(isBadVersion(c)):
                r=c
            else:
                l=c

    
                        
            

                
            
a=Solution()
print(a.firstBadVersion(3))
